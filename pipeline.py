from config import T_Q, T_R
from classifier import input_classifier, output_classifier
from model import generate_response

def defense_pipeline(prompt: str) -> dict:
    """
    Run input classifier > model > output classifier.
    ic - input classifier score
    oc - output classifier score
    """
    
    ic_score = input_classifier(prompt)
    if ic_score >= T_Q:
        return {
            "prompt": prompt,
            "ic_score": ic_score,
            "model_output": "",
            "oc_score": None,
            "decision": "blocked",
            "blocked_stage": "input"
        }
    
    model_output = generate_response(prompt)
    oc_score = output_classifier(model_output)
    if oc_score >= T_R:
        return {
            "prompt": prompt,
            "ic_score": ic_score,
            "model_output": model_output,
            "oc_score": oc_score,
            "decision": "blocked",
            "blocked_stage": "output"
        }
    
    return {
        "prompt": prompt,
        "ic_score": ic_score,
        "model_output": model_output,
        "oc_score": oc_score,
        "decision": "passed",
        "blocked_stage": None
    }


