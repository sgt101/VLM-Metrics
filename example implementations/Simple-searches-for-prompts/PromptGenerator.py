"""
PromptGenerator: LLM-Based Prompt Optimization

This module implements a prompt optimization framework that uses an LLM to generate
variations of a base prompt, then evaluates and optimizes them using beam search.

Unlike TreeSearch which selects examples from a dataset, PromptGenerator creates
entirely new prompt variations using an LLM's creative capabilities.

Key Features:
- LLM-powered prompt variation generation
- Beam search optimization with pruning
- Batch API evaluation for cost-effective parallel processing
- Support for multiple LLM providers (OpenAI, etc.)
- Progress tracking and result logging

Typical usage:
    from PromptGenerator import PromptGenerator
    
    # Initialize with base prompt
    generator = PromptGenerator(
        base_prompt="You are a helpful assistant that writes code documentation.",
        generator_model="gpt-4",
        evaluator_model="gpt-3.5-turbo",
        metric=similarity_metric
    )
    
    # Run optimization
    best_prompt = generator.optimize(evaluation_set=test_cases)

Author: [Add author]
License: [Add license]
"""

import random
import json
from typing import Dict, List, Optional, Callable
from time import sleep
import datetime
from pathlib import Path
import logging
from statistics import median, mean
import copy
import pandas as pd
from openai import OpenAI

_logger = logging.getLogger("prompt_generator")


class PromptGenerator:
    """
    LLM-based prompt optimization using beam search.
    
    Generates variations of a base prompt using an LLM, evaluates them on a test set,
    and iteratively refines to find the optimal prompt.
    
    Attributes:
        _base_prompt (str): Original prompt to generate variations from
        _generator_client (OpenAI): Client for prompt generation
        _evaluator_client (OpenAI): Client for prompt evaluation
        _generator_model (str): Model name for generation (e.g., "gpt-4")
        _evaluator_model (str): Model name for evaluation
        _metric (callable): Function to evaluate prompt quality
        _breadth (int): Number of variations per iteration
        _max_rounds (int): Maximum optimization iterations
        _pruning_threshold (float): Threshold for pruning poor variations
        _temperature (float): Temperature for variation generation
        _results_file (str): Path to results file
    """
    
    def __init__(
        self,
        base_prompt: str,
        generator_model: str = "gpt-4",
        evaluator_model: str = "gpt-3.5-turbo",
        metric: Optional[Callable] = None,
        breadth: int = 100,
        max_rounds: int = 5,
        pruning_threshold: float = 0.03,
        temperature: float = 0.7,
        generator_api_key: Optional[str] = None,
        evaluator_api_key: Optional[str] = None
    ):
        """
        Initialize the PromptGenerator.
        
        Args:
            base_prompt: Starting prompt to create variations from
            generator_model: LLM model for generating variations (default: "gpt-4")
            evaluator_model: LLM model for evaluation (default: "gpt-3.5-turbo")
            metric: Function to evaluate prompt quality (expected, predicted) -> float
            breadth: Number of variations to generate per iteration (default: 10)
            max_rounds: Maximum optimization iterations (default: 5)
            pruning_threshold: Fitness gap for pruning (default: 0.03)
            temperature: Creativity level for generation (default: 0.7)
            generator_api_key: Optional API key for generator (uses env var if None)
            evaluator_api_key: Optional API key for evaluator (uses env var if None)
        """
        self._base_prompt = base_prompt
        self._generator_model = generator_model
        self._evaluator_model = evaluator_model
        self._metric = metric
        self._breadth = breadth
        self._max_rounds = max_rounds
        self._pruning_threshold = pruning_threshold
        self._temperature = temperature
        
        # Initialize OpenAI clients
        if generator_api_key:
            self._generator_client = OpenAI(api_key=generator_api_key)
        else:
            self._generator_client = OpenAI()
            
        if evaluator_api_key:
            self._evaluator_client = OpenAI(api_key=evaluator_api_key)
        else:
            self._evaluator_client = OpenAI()
        
        # Setup results tracking
        self._run_start = str(datetime.datetime.now()).replace(':', '-').replace(' ', '_')
        self._results_file = Path.cwd().joinpath("results", f"prompt_gen_{self._run_start}.json")
        self._results_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Setup prompt logging
        self._prompt_log_file = Path.cwd().joinpath("results", f"prompts_{self._run_start}.csv")
        self._init_prompt_log()
        
    def generate_variations(self, prompt: str, num_variations: int) -> List[str]:
        """
        Generate variations of a prompt using the generator LLM.
        
        Args:
            prompt: The prompt to create variations from
            num_variations: Number of variations to generate
            
        Returns:
            List of prompt variations
            
        Example:
            >>> variations = generator.generate_variations("You are helpful.", 5)
            >>> len(variations)
            5
        """
        system_message = """You are an expert prompt engineer. Your task is to generate creative variations of a given prompt.

Each variation should:
- Maintain the core intent of the original prompt
- Use different wording, structure, or approach
- Be practical and effective for the intended use case
- Explore different styles (concise, detailed, formal, casual, etc.)

Generate EXACTLY the requested number of variations, each on a new line.
Output ONLY the variations, nothing else."""

        user_message = f"""Original prompt:
{prompt}

Generate {num_variations} creative variations of this prompt."""

        try:
            response = self._generator_client.chat.completions.create(
                model=self._generator_model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=self._temperature,
                max_tokens=2000
            )
            
            # Parse variations from response
            content = response.choices[0].message.content
            variations = [v.strip() for v in content.split('\n') if v.strip()]
            
            # Ensure we have the right number
            if len(variations) < num_variations:
                _logger.warning(f"Generated only {len(variations)} of {num_variations} requested variations")
            
            return variations[:num_variations]
            
        except Exception as e:
            _logger.error(f"Error generating variations: {e}")
            # Fallback: return slight modifications of the original
            return [f"{prompt} (variation {i+1})" for i in range(num_variations)]
    
    def _init_prompt_log(self):
        """Initialize the prompt log file with headers."""
        with open(self._prompt_log_file, 'w') as f:
            f.write("Round,Variation,Fitness,Prompt\n")
        print(f"📝 Logging prompts to: {self._prompt_log_file}")
    
    def _log_prompt(self, round_num: int, variation_num: int, fitness: float, prompt: str):
        """
        Log a tested prompt in compact CSV format.
        
        Args:
            round_num: Optimization round number
            variation_num: Variation number within round
            fitness: Fitness score achieved
            prompt: The prompt text (truncated if too long)
        """
        # Truncate prompt for readability, keep first 100 chars
        prompt_preview = prompt.replace('\n', ' ').replace('"', '""')[:100]
        if len(prompt) > 100:
            prompt_preview += "..."
        
        with open(self._prompt_log_file, 'a') as f:
            f.write(f"{round_num},{variation_num},{fitness:.4f},\"{prompt_preview}\"\n")
    
    def _create_batch_requests(self, prompts: List[str], evaluation_set: List[Dict], round_num: int) -> str:
        """
        Create a JSONL file with batch requests for all prompt-example combinations.
        
        Args:
            prompts: List of prompts to evaluate
            evaluation_set: Test cases to evaluate on
            round_num: Current round number
            
        Returns:
            Path to the created JSONL file
        """
        batch_file = self._results_file.parent / f"batch_requests_round_{round_num}_{self._run_start}.jsonl"
        
        with open(batch_file, 'w') as f:
            for prompt_idx, prompt in enumerate(prompts):
                for example_idx, example in enumerate(evaluation_set):
                    # Create unique ID for tracking
                    custom_id = f"r{round_num}_p{prompt_idx}_e{example_idx}"
                    
                    request = {
                        "custom_id": custom_id,
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": self._evaluator_model,
                            "messages": [
                                {"role": "system", "content": prompt},
                                {"role": "user", "content": example['input']}
                            ],
                            "temperature": 0.3,
                            "max_tokens": 1000
                        }
                    }
                    f.write(json.dumps(request) + '\n')
        
        print(f"📦 Created batch file: {batch_file}")
        return str(batch_file)
    
    def _submit_and_wait_batch(self, batch_file: str) -> pd.DataFrame:
        """
        Submit batch file to OpenAI and wait for completion.
        
        Args:
            batch_file: Path to JSONL batch request file
            
        Returns:
            DataFrame with results (custom_id, response)
        """
        print(f"📤 Uploading batch file...")
        
        # Upload file
        with open(batch_file, 'rb') as f:
            batch_input_file = self._evaluator_client.files.create(
                file=f,
                purpose="batch"
            )
        
        print(f"✓ File uploaded: {batch_input_file.id}")
        
        # Create batch
        batch = self._evaluator_client.batches.create(
            input_file_id=batch_input_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={"description": "prompt_optimization"}
        )
        
        print(f"🔄 Batch submitted: {batch.id}")
        print(f"   Status: {batch.status}")
        
        # Poll for completion
        import time
        poll_interval = 10  # seconds
        
        while batch.status not in ["completed", "failed", "expired", "cancelled"]:
            time.sleep(poll_interval)
            batch = self._evaluator_client.batches.retrieve(batch.id)
            print(f"   Status: {batch.status} | Progress: {batch.request_counts.completed}/{batch.request_counts.total}")
        
        if batch.status != "completed":
            raise Exception(f"Batch failed with status: {batch.status}")
        
        print(f"✓ Batch completed!")
        
        # Download results
        result_file_id = batch.output_file_id
        result_content = self._evaluator_client.files.content(result_file_id)
        
        # Parse results
        results = []
        for line in result_content.text.strip().split('\n'):
            results.append(json.loads(line))
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        df['message'] = df['response'].apply(
            lambda x: x['body']['choices'][0]['message']['content'] if 'body' in x else ''
        )
        
        return df[['custom_id', 'message']]
    
    def _score_batch_results(self, results_df: pd.DataFrame, prompts: List[str], 
                            evaluation_set: List[Dict], round_num: int) -> List[float]:
        """
        Score batch results and compute fitness for each prompt.
        
        Args:
            results_df: DataFrame with batch results
            prompts: List of prompts that were evaluated
            evaluation_set: Test cases used
            round_num: Current round number
            
        Returns:
            List of fitness scores (one per prompt)
        """
        fitness_scores = []
        
        for prompt_idx, prompt in enumerate(prompts):
            total_fitness = 0.0
            count = 0
            
            for example_idx, example in enumerate(evaluation_set):
                custom_id = f"r{round_num}_p{prompt_idx}_e{example_idx}"
                
                # Find result for this combination
                result_row = results_df[results_df['custom_id'] == custom_id]
                
                if not result_row.empty:
                    prediction = result_row.iloc[0]['message']
                    
                    # Evaluate using metric
                    if self._metric:
                        fitness = self._metric(example['expected'], prediction)
                        total_fitness += fitness
                        count += 1
            
            # Calculate average fitness for this prompt
            avg_fitness = total_fitness / count if count > 0 else 0.0
            fitness_scores.append(avg_fitness)
            
            # Log the prompt
            self._log_prompt(round_num, prompt_idx + 1, avg_fitness, prompt)
        
        return fitness_scores
    
    def evaluate_prompts_batch(self, prompts: List[str], evaluation_set: List[Dict], 
                              round_num: int) -> List[float]:
        """
        Evaluate multiple prompts using OpenAI's batch API.
        
        Args:
            prompts: List of prompts to evaluate
            evaluation_set: Test cases to evaluate on
            round_num: Current round number
            
        Returns:
            List of fitness scores (one per prompt)
        """
        print(f"\n🔬 Evaluating {len(prompts)} prompts on {len(evaluation_set)} examples using batch API...")
        
        # Create batch requests
        batch_file = self._create_batch_requests(prompts, evaluation_set, round_num)
        
        # Submit and wait
        results_df = self._submit_and_wait_batch(batch_file)
        
        # Score results
        fitness_scores = self._score_batch_results(results_df, prompts, evaluation_set, round_num)
        
        return fitness_scores
    
    def evaluate_prompt(
        self, 
        prompt: str, 
        evaluation_set: List[Dict],
        highest_fitness: float = 0.0,
        round_num: int = 0,
        variation_num: int = 0
    ) -> float:
        """
        Evaluate a prompt on the evaluation set.
        
        Args:
            prompt: The prompt to evaluate
            evaluation_set: List of test cases with 'input' and 'expected' keys
            highest_fitness: Current best fitness for pruning decisions
            round_num: Current optimization round (for logging)
            variation_num: Variation number within round (for logging)
            
        Returns:
            Average fitness score across evaluation set
            
        Note:
            Implements early stopping if prompt performs poorly compared to best.
        """
        total_fitness = 0.0
        count = 0
        
        for i, example in enumerate(evaluation_set):
            # Call evaluator model with the prompt
            try:
                response = self._evaluator_client.chat.completions.create(
                    model=self._evaluator_model,
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": example['input']}
                    ],
                    temperature=0.3,
                    max_tokens=1000
                )
                
                prediction = response.choices[0].message.content
                
                # Evaluate using metric
                if self._metric:
                    fitness = self._metric(example['expected'], prediction)
                    total_fitness += fitness
                    count += 1
                    
                    # Early stopping if performing poorly
                    if count > 5 and (total_fitness / count) < (highest_fitness - self._pruning_threshold):
                        _logger.info(f"Early stopping: avg fitness {total_fitness/count:.3f} < threshold {highest_fitness - self._pruning_threshold:.3f}")
                        return 0.0
                        
            except Exception as e:
                _logger.error(f"Error evaluating example {i}: {e}")
                continue
        
        final_fitness = total_fitness / count if count > 0 else 0.0
        
        # Log this prompt test
        self._log_prompt(round_num, variation_num, final_fitness, prompt)
        
        return final_fitness
    
    def optimize(
        self,
        evaluation_set: List[Dict],
        initial_variations: Optional[List[str]] = None
    ) -> Dict:
        """
        Run the optimization loop to find the best prompt.
        
        Args:
            evaluation_set: List of test cases with 'input' and 'expected' keys
            initial_variations: Optional starting variations (generates if None)
            
        Returns:
            Dictionary with:
                - 'best_prompt': The highest-scoring prompt
                - 'best_fitness': The fitness score
                - 'all_results': List of all evaluated prompts and scores
                
        Example:
            >>> test_cases = [
            ...     {'input': 'def add(a, b): return a + b', 
            ...      'expected': 'Adds two numbers'}
            ... ]
            >>> result = generator.optimize(test_cases)
            >>> print(result['best_prompt'])
        """
        if not self._metric:
            raise ValueError("Metric function must be provided")
        
        # Initialize
        if initial_variations:
            current_prompts = initial_variations[:self._breadth]
        else:
            current_prompts = self.generate_variations(self._base_prompt, self._breadth)
        
        best_prompt = self._base_prompt
        best_fitness = 0.0
        all_results = []
        
        # Write parameters
        self._write_params()
        
        # Optimization loop
        for round_num in range(self._max_rounds):
            print(f"\n=== Round {round_num + 1}/{self._max_rounds} ===")
            
            # Evaluate all prompts in this round using batch API
            fitness_scores = self.evaluate_prompts_batch(current_prompts, evaluation_set, round_num)
            
            # Create results for this round
            round_results = []
            for i, (prompt, fitness) in enumerate(zip(current_prompts, fitness_scores)):
                result = {
                    'round': round_num,
                    'prompt': prompt,
                    'fitness': fitness
                }
                round_results.append(result)
                all_results.append(result)
                
                # Update best
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_prompt = prompt
                    print(f"✓ New best fitness: {best_fitness:.4f} (variation {i+1})")
                
                # Save intermediate results
                self._save_result(result)
            
            # Sort by fitness
            round_results.sort(key=lambda x: x['fitness'], reverse=True)
            
            # Select top performers for next round
            top_k = max(1, self._breadth // 3)
            top_prompts = [r['prompt'] for r in round_results[:top_k]]
            
            # Generate new variations from top performers
            if round_num < self._max_rounds - 1:
                next_prompts = []
                variations_per_prompt = self._breadth // len(top_prompts)
                
                for top_prompt in top_prompts:
                    variations = self.generate_variations(top_prompt, variations_per_prompt)
                    next_prompts.extend(variations)
                
                # Fill remaining slots with variations of best
                while len(next_prompts) < self._breadth:
                    next_prompts.extend(self.generate_variations(best_prompt, 1))
                
                current_prompts = next_prompts[:self._breadth]
        
        # Final results
        final_result = {
            'best_prompt': best_prompt,
            'best_fitness': best_fitness,
            'all_results': all_results,
            'rounds': self._max_rounds,
            'total_evaluations': len(all_results)
        }
        
        self._save_final_results(final_result)
        
        return final_result
    
    def _write_params(self):
        """Write optimization parameters to results file."""
        params = {
            'base_prompt': self._base_prompt,
            'generator_model': self._generator_model,
            'evaluator_model': self._evaluator_model,
            'breadth': self._breadth,
            'max_rounds': self._max_rounds,
            'pruning_threshold': self._pruning_threshold,
            'temperature': self._temperature,
            'run_start': self._run_start
        }
        
        with open(self._results_file, 'w') as f:
            f.write(json.dumps({'parameters': params}) + '\n')
    
    def _save_result(self, result: Dict):
        """Append a result to the results file."""
        with open(self._results_file, 'a') as f:
            f.write(json.dumps(result) + '\n')
    
    def _save_final_results(self, final_result: Dict):
        """Save final optimization results."""
        final_file = self._results_file.parent / f"final_{self._results_file.name}"
        with open(final_file, 'w') as f:
            json.dump(final_result, f, indent=2)
        
        print(f"\n✓ Results saved to {final_file}")
