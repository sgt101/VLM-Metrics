"""
Example usage of PromptGenerator for LLM-based prompt optimization.

This script demonstrates how to use the PromptGenerator class to optimize
prompts using an LLM to generate variations.
"""

from PromptGenerator import PromptGenerator
from sentence_transformers import SentenceTransformer, util

# Setup similarity metric
model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")

def sentence_similarity(expected: str, predicted: str) -> float:
    """
    Calculate cosine similarity between expected and predicted text.
    
    Args:
        expected: Ground truth text
        predicted: Model-generated text
        
    Returns:
        Similarity score between 0 and 1
    """
    exp_emb = model.encode([expected], convert_to_tensor=True)
    pred_emb = model.encode([predicted], convert_to_tensor=True)
    return util.pytorch_cos_sim(exp_emb, pred_emb).item()


# Example 1: Code Documentation Task
def example_code_documentation(num_examples=10):
    """
    Optimize a prompt for generating code documentation using Java examples.
    
    Args:
        num_examples: Number of examples to use for evaluation (default: 10)
    """
    import pandas as pd
    
    base_prompt = "You are a helpful assistant that writes clear and concise code documentation."
    
    # Load Java code-documentation pairs from eval.csv
    print(f"Loading {num_examples} examples from eval.csv...")
    df = pd.read_csv("eval.csv", index_col=0)
    
    # Convert to evaluation set format
    evaluation_set = []
    for i, (idx, row) in enumerate(df.head(num_examples).iterrows()):
        evaluation_set.append({
            'input': row['question'],   # Java code
            'expected': row['answer']    # Documentation
        })
    
    print(f"Loaded {len(evaluation_set)} Java code examples for evaluation")
    
    # Initialize generator
    generator = PromptGenerator(
        base_prompt=base_prompt,
        generator_model="gpt-4",
        evaluator_model="gpt-3.5-turbo",
        metric=sentence_similarity,
        breadth=100,
        max_rounds=10,
        temperature=0.8
    )
    
    # Run optimization
    print("Starting prompt optimization for code documentation...")
    result = generator.optimize(evaluation_set)
    
    print("\n" + "="*80)
    print("OPTIMIZATION COMPLETE")
    print("="*80)
    print(f"\nBest Fitness: {result['best_fitness']:.4f}")
    print(f"Total Evaluations: {result['total_evaluations']}")
    print(f"\nBest Prompt:\n{result['best_prompt']}")
    
    return result


# Example 2: Question Answering Task
def example_question_answering():
    """Optimize a prompt for question answering."""
    
    base_prompt = "You are a knowledgeable assistant that provides accurate and helpful answers."
    
    evaluation_set = [
        {
            'input': 'What is the capital of France?',
            'expected': 'Paris'
        },
        {
            'input': 'How does photosynthesis work?',
            'expected': 'Photosynthesis is the process by which plants convert light energy into chemical energy, using carbon dioxide and water to produce glucose and oxygen.'
        },
        {
            'input': 'What is the Pythagorean theorem?',
            'expected': 'The Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides: a² + b² = c²'
        }
    ]
    
    generator = PromptGenerator(
        base_prompt=base_prompt,
        generator_model="gpt-4",
        evaluator_model="gpt-3.5-turbo",
        metric=sentence_similarity,
        breadth=8,
        max_rounds=4
    )
    
    print("Starting prompt optimization for question answering...")
    result = generator.optimize(evaluation_set)
    
    print(f"\nBest Prompt: {result['best_prompt']}")
    print(f"Best Fitness: {result['best_fitness']:.4f}")
    
    return result


# Example 3: Using Custom Variations
def example_custom_variations():
    """Start optimization with custom initial variations."""
    
    base_prompt = "You are a helpful coding assistant."
    
    # Provide custom starting variations
    initial_variations = [
        "You are an expert programmer who writes clean, efficient code.",
        "You are a senior software engineer providing code assistance.",
        "You are a coding mentor helping developers write better code.",
        "You are a technical expert specializing in software development.",
    ]
    
    evaluation_set = [
        {
            'input': 'Write a function to reverse a string',
            'expected': 'def reverse_string(s):\n    return s[::-1]'
        }
    ]
    
    generator = PromptGenerator(
        base_prompt=base_prompt,
        metric=sentence_similarity,
        breadth=4,
        max_rounds=2
    )
    
    result = generator.optimize(
        evaluation_set=evaluation_set,
        initial_variations=initial_variations
    )
    
    print(f"\nStarted with {len(initial_variations)} custom variations")
    print(f"Best result: {result['best_fitness']:.4f}")
    
    return result


if __name__ == "__main__":
    print("PromptGenerator Examples\n")
    
    # Run example
    print("\n" + "="*80)
    print("Example 1: Code Documentation")
    print("="*80)
    
    # You can specify how many examples to use (7,453 available in eval.csv):
    example_code_documentation(num_examples=10)  # Use 10 Java examples

    
    # Uncomment to run other examples:
    # example_question_answering()
    # example_custom_variations()
