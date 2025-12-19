"""
Quick example demonstrating the prompt logging feature.

Run this to see how prompts are logged to a CSV file.
"""

from PromptGenerator import PromptGenerator

# Simple exact match metric for demo
def exact_match(expected: str, predicted: str) -> float:
    """Simple metric: 1.0 if exact match, 0.0 otherwise."""
    return 1.0 if expected.strip().lower() == predicted.strip().lower() else 0.0

# Initialize generator
generator = PromptGenerator(
    base_prompt="You are a helpful assistant.",
    generator_model="gpt-3.5-turbo",  # Using cheaper model for demo
    evaluator_model="gpt-3.5-turbo",
    metric=exact_match,
    breadth=3,  # Small breadth for quick demo
    max_rounds=2  # Just 2 rounds
)

# Simple evaluation set
eval_set = [
    {
        'input': 'What is 2+2?',
        'expected': '4'
    },
    {
        'input': 'What color is the sky?',
        'expected': 'blue'
    }
]

print("Running optimization with prompt logging...")
print("=" * 60)

result = generator.optimize(eval_set)

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Best Prompt: {result['best_prompt']}")
print(f"Best Fitness: {result['best_fitness']:.4f}")
print(f"\nPrompt log saved to: results/prompts_*.csv")
print("\nView the CSV file to see all tested prompts!")
print("\nCSV Format:")
print("  Round | Variation | Fitness | Prompt (first 100 chars)")
print("  ------|-----------|---------|-------------------------")
print("  0     | 1         | 0.5000  | You are a helpful and friendly assistant...")
print("  0     | 2         | 0.7500  | You are an expert assistant that provides...")
