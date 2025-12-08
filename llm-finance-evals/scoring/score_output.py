import yaml
import json

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def score_response(model_output, golden_answer, schema, rubric):
    """
    Simple heuristic comparison:
    - Checks overlap between model_output and golden_answer for each component.
    - Not meant to be production; designed to illustrate how scoring works.
    """

    results = {}
    for component in schema["components"]:
        name = component["name"]

        # Super simple heuristic: count keyword overlap
        keywords = name.split("_")
        overlap = sum(1 for kw in keywords if kw in model_output.lower())
        score = 1 if overlap == 0 else (3 if overlap == 1 else 5)

        results[name] = score

    return results

if __name__ == "__main__":
    # Example usage
    schema = load_yaml("scoring/schema.yaml")
    rubric = load_yaml("scoring/rubric_long_short.yaml")

    model_output = open("example_model_output.txt").read()
    golden_answer = open("example_golden_answer.txt").read()

    scored = score_response(model_output, golden_answer, schema, rubric)
    print(json.dumps(scored, indent=2))
