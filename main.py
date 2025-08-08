import csv
from config import NUM_PROMPTS, RESULTS_FILE
from pipeline import defense_pipeline

# Example prompts (in real case, this will be a dataset)
prompts = [f"Prompt {i}" for i in range(1, NUM_PROMPTS + 1)]

results = []
for prompt in prompts:
    result = defense_pipeline(prompt)
    results.append(result)
    print(result)

# Save results to CSV
with open(RESULTS_FILE, mode="w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to {RESULTS_FILE}")
