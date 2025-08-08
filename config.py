"""
Config for Defense Pipeline (matches paper's notation):
- T_Q: Input classifier threshold (t_q in paper)
- T_R: Output classifier threshold (t_r in paper)
- NUM_PROMPTS: Number of prompts for mock run
- RESULTS_FILE: Where pipeline decisions are logged
"""

# Thresholds for harm scores (0 to 1)
T_Q = 0.5  # Input classifier (user prompt)
T_R = 0.5  # Output classifier (model reply)

# Number of prompts to test
NUM_PROMPTS = 10

# Output CSV file
RESULTS_FILE = "results.csv"
