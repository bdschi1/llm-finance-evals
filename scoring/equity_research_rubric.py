"""
Equity research rubric scoring

This module implements a simple rubric-based scorer for the
`equity_research_v1` eval defined in `evals/equity_research_eval.yaml`.

It is intentionally simple and transparent so that:
- PMs / domain experts can read the dimensions in plain English.
- Engineers can later wire this into a larger eval framework or API.

The basic pattern:
- You pass in a model output (thesis text) and, optionally, a golden answer.
- The scorer returns:
  - raw per-dimension scores (1–5),
  - a weighted overall score (0–5),
  - and free-text comments where appropriate.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class RubricDimension:
    id: str
    label: str
    weight: float  # weight as a fraction of 1.0


# These weights match the YAML config in evals/equity_research_eval.yaml
EQUITY_RESEARCH_DIMENSIONS = [
    RubricDimension(
        id="business_understanding",
        label="Business understanding",
        weight=0.30,
    ),
    RubricDimension(
        id="thesis_clarity",
        label="Thesis clarity and structure",
        weight=0.25,
    ),
    RubricDimension(
        id="drivers_and_edge",
        label="Drivers and edge",
        weight=0.25,
    ),
    RubricDimension(
        id="risk_discussion",
        label="Risk discussion",
        weight=0.20,
    ),
]


def _normalize_score(score: float) -> float:
    """
    Force scores into the 1–5 range.
    """
    return max(1.0, min(5.0, float(score)))


def score_equity_thesis(
    model_output: str,
    golden_answer: Optional[str] = None,
    notes: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Score a single equity research thesis according to the rubric.

    For now, this is intentionally a stub:

    - It returns neutral (3.0) scores for all dimensions.
    - It is designed so that a human reviewer or future heuristics/LLM-judge
      can populate the dimension scores.

    Parameters
    ----------
    model_output : str
        The thesis text produced by the model.
    golden_answer : str, optional
        Reference "golden" answer. Not used yet, but kept for future logic.
    notes : str, optional
        Free-text notes from a human reviewer.

    Returns
    -------
    Dict[str, Any]
        {
          "dimensions": {
             "<dimension_id>": {"score": float, "weight": float}
          },
          "overall_score": float,
          "model_output": str,
          "golden_answer": str or None,
          "reviewer_notes": str or None,
        }
    """
    # TODO: replace this with actual heuristics or LLM-as-judge logic.
    base_score = 3.0

    dimension_scores: Dict[str, Dict[str, float]] = {}
    overall = 0.0

    for dim in EQUITY_RESEARCH_DIMENSIONS:
        s = _normalize_score(base_score)
        dimension_scores[dim.id] = {
            "score": s,
            "weight": dim.weight,
        }
        overall += s * dim.weight

    result: Dict[str, Any] = {
        "dimensions": dimension_scores,
        "overall_score": overall,
        "model_output": model_output,
        "golden_answer": golden_answer,
        "reviewer_notes": notes,
    }
    return result
