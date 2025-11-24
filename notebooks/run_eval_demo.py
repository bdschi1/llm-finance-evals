"""
run_eval_demo.py

Simple demo script that wires together:
- input data from /data
- golden answers from /golden_answers
- rubric-based scoring functions from /scoring

The goal is to show, in a transparent way, how an engineer could:
- load a case,
- obtain or generate a model output,
- and score it using the rubric logic.

This is intentionally minimal and uses the golden answers as a stand-in
for model outputs, so the scoring path is exercised even before any
model integration.
"""

import json
from pathlib import Path

from scoring.equity_research_rubric import score_equity_thesis
from scoring.risk_logic_rubric import score_risk_summary


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def demo_equity_research_case(root: Path):
    """
    Demo for `equity_research_v1` using ER case 1.
    """
    print("=" * 80)
    print("Equity research eval – ER case 1")
    print("=" * 80)

    data_path = root / "data" / "equity" / "er_case_1_input.json"
    golden_path = root / "golden_answers" / "er_case_1_answer.md"

    case_data = load_json(data_path)
    golden_answer = load_text(golden_path)

    # In a real workflow, you would call an LLM here with `case_data` to obtain `model_output`.
    # For this wiring demo, we simply pretend the model output equals the golden answer.
    model_output = golden_answer

    result = score_equity_thesis(
        model_output=model_output,
        golden_answer=golden_answer,
        notes="Demo run using golden answer as model output.",
    )

    print("Per-dimension scores:")
    for dim_id, info in result["dimensions"].items():
        print(f"  - {dim_id}: score={info['score']} (weight={info['weight']})")

    print(f"\nOverall score: {result['overall_score']:.2f} (0–5 scale)")
    print()


def demo_risk_logic_case(root: Path):
    """
    Demo for `risk_logic_v1` using Risk case 1.
    """
    print("=" * 80)
    print("Risk logic eval – Risk case 1")
    print("=" * 80)

    data_path = root / "data" / "risk" / "risk_case_1_input.json"
    golden_path = root / "golden_answers" / "risk_case_1_answer.md"

    case_data = load_json(data_path)
    golden_answer = load_text(golden_path)

    # Again, in a real setup this would be the model's risk summary.
    model_output = golden_answer

    result = score_risk_summary(
        model_output=model_output,
        golden_answer=golden_answer,
        notes="Demo run using golden answer as model output.",
    )

    print("Per-dimension scores:")
    for dim_id, info in result["dimensions"].items():
        print(f"  - {dim_id}: score={info['score']} (weight={info['weight']})")

    print(f"\nOverall score: {result['overall_score']:.2f} (0–5 scale)")
    print()


def main():
    # Assume this script is run from the repo root:
    #   python notebooks/run_eval_demo.py
    # `root` is the repository root directory.
    root = Path(__file__).resolve().parents[1]

    demo_equity_research_case(root)
    demo_risk_logic_case(root)


if __name__ == "__main__":
    main()
