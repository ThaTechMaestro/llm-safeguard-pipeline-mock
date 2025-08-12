# LLM Safeguard Pipeline (Mock)

This repository contains a **mock implementation** of the safeguard pipeline described in *Adversarial Attacks on the LLM Safeguard Pipeline* (2025).  
It models a two-stage filtering architecture, **input classifier** and **output classifier**, used to reduce the risk of harmful outputs in LLM deployments.

The focus is on **architecture clarity** and **defensive reasoning**, not production-grade code.  
It is intended as a **research sandbox** for studying attack surfaces, tuning thresholds, and prototyping mitigations.



## Context

Modern LLM safeguard pipelines often adopt a **defense-in-depth** strategy:

```

User Prompt
   ↓
Input Classifier (IC) → block if score ≥ T_Q
   ↓
Target Model (mock)
   ↓
Output Classifier (OC) → block if score ≥ T_R
   ↓
Final Output (or refusal)

````

Where:

- **T_Q** – Input classifier threshold  
- **T_R** – Output classifier threshold  
- Both thresholds ∈ [0,1] and are configurable in `config.py`.

This mirrors the architecture discussed in the paper while remaining safe for open experimentation.


## Objectives

- Provide a **minimal, transparent reference** for a safeguard pipeline.  
- Enable **controlled experiments** on attack strategies (e.g., step-by-step jailbreaks).  
- Support **threshold calibration exercises** to balance safety and usability. 

## Phase Progression

This repository is part of a **multi-phase engineering track** toward a full-scale, real-model safeguard system.

**Phase 1 – Mock Pipeline (Current)**  
- Implement two-stage safeguard logic with mock classifiers and model.  
- Validate decision flow and blocking behavior.  
- Establish configurable thresholds and logging.  
- Repo: [llm-safeguard-pipeline-mock](https://github.com/ThaTechMaestro/llm-safeguard-pipeline-mock)

**Phase 2 – Threat Models & STACK Attack Mock**   
- Implement mock STACK attack logic (front-to-back, transfer).  
- Simulate attacker access levels (black-box, semi-separable, inseparable).  
- Measure impact on IC and OC separately.  
- Repo: [llm-safeguard-stack-attack-mock](https://github.com/ThaTechMaestro/llm-safeguard-stack-attack-mock)

**Phase 3 – Confirm Universal Jailbreak Module** 
- Implement universal jailbreak (“Confirm” prompt) from paper.  
- Test bypass effectiveness against IC and OC in the mock pipeline.  
- Compare ASR (Attack Success Rate) with STACK results.  
- Repo: `llm-safeguard-confirm-mock`

**Phase 4 – Calibration & Threshold Experiments**  
- Replicate paper’s threshold tuning for target refusal rates.  
- Measure tradeoffs between blocking harmful and benign prompts.  
- Repo: `llm-safeguard-threshold-calibration`

**Phase 5 – Attack Success Rate Reproduction**  
- Simulate experiments from paper to reproduce reported metrics.  
- Repo: `llm-safeguard-attack-metrics`

**Phase 6 – Combined System & Dashboard**  
- Integrate pipeline, STACK, Confirm, and calibration into one repo.  
- Add visualization for threat models, blocked stages, ASR.  
- Repo: `llm-safeguard-simulator` 

## File Structure

- `config.py` – system configuration (thresholds, constants)  
- `classifier.py` – mock input/output classifiers (scoring functions)  
- `model.py` – mock LLM generator (placeholder for target model)  
- `pipeline.py` – defense pipeline logic  
- `main.py` – entry point to run the pipeline on sample prompts  



## How to Run


```bash
# Clone repository
git clone https://github.com/ThaTechMaestro/llm-safeguard-pipeline-mock
cd llm-safeguard-pipeline-mock

# Runs on sample prompts
python main.py
````

Results are stored in `results.csv` with details for each stage (scores, decision, blocked stage).



## Reference

[*Adversarial Attacks on the LLM Safeguard Pipeline* (2025)](https://arxiv.org/abs/2506.24068)



## Notes

This repo is **deliberately simplified** for study purposes.
Real-world safeguard/defense systems involve more complex classifiers, multi-modal inputs, and dynamic policy enforcement.
The mock design here provides a starting point for reasoning about **attack surfaces**, **compositional defenses**, and **trust engineering** at scale.
