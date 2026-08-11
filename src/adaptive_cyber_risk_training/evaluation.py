from __future__ import annotations


def skill_transfer_index(pre_score: float, post_score: float, transfer_score: float) -> float:
    """Compute a simple learning-transfer index from normalized scores."""
    for value in (pre_score, post_score, transfer_score):
        if not 0 <= value <= 1:
            raise ValueError("scores must be between 0 and 1")
    improvement = max(0.0, post_score - pre_score)
    return round((0.6 * improvement) + (0.4 * transfer_score), 3)


def engagement_summary(confidence: float, perceived_realism: float, usefulness: float) -> float:
    """Average learner-reported engagement indicators."""
    values = [confidence, perceived_realism, usefulness]
    if any(not 0 <= value <= 1 for value in values):
        raise ValueError("engagement scores must be between 0 and 1")
    return round(sum(values) / len(values), 3)
