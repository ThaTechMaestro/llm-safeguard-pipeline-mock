import random

def input_classifier(prompt: str) -> float:
    """Mock input classifier returning a harm score between 0 and 1."""
    return random.uniform(0, 1)

def output_classifier(response: str) -> float:
    """Mock output classifier returning a harm score between 0 and 1."""
    return random.uniform(0, 1)
