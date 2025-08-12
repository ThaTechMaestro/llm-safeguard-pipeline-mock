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
- Repo: [Link](https://github.com/ThaTechMaestro/llm-safeguard-pipeline-mock)

**Phase 2 – Attack Simulation **  
- Implement mock STACK and transfer-STACK attack logic.  
- Measure impact on IC and OC separately.  
- Capture results in structured metrics.
- Repo: [Link](https://github.com/ThaTechMaestro/llm-safeguard-stack-attack-mock)

**Phase 3 – Real Model Integration**  
- Swap mock model for a small, cost-efficient LLM (e.g., Mistral-7B).  
- Replace mock classifiers with lightweight fine-tuned safety classifiers.  
- Run real-world adversarial prompts and collect statistics.

**Phase 4 – Scaling & Automation**  
- Integrate with asynchronous job queues for batch evaluation.  
- Add telemetry, scoring dashboards, and automated reporting.  
- Begin resilience tuning with adaptive thresholds.

**Phase 5 – Production-Grade Safeguard Stack**  
- Harden architecture for deployment in trust-critical AI systems.  

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
