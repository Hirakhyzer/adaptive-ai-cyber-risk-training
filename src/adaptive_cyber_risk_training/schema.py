from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class LearnerLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class LearnerProfile(BaseModel):
    learner_id: str
    level: LearnerLevel
    target_skill: str
    prior_errors: list[str] = Field(default_factory=list)
    support_needs: list[str] = Field(default_factory=list)


class CyberRiskScenario(BaseModel):
    scenario_id: str
    learner_level: LearnerLevel
    sector: str
    learning_objective: str
    asset_context: list[str]
    threat_context: str
    existing_controls: list[str]
    risk_prompt: str
    expected_outputs: list[str]
    adaptation_focus: str
    safety_boundary: str = "Risk assessment only; no exploit steps, payloads, or intrusion instructions."

    @field_validator("asset_context", "existing_controls", "expected_outputs")
    @classmethod
    def require_non_empty_list(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("scenario lists must not be empty")
        return value


class QualityReport(BaseModel):
    scenario_id: str
    correctness: float
    consistency: float
    pedagogical_alignment: float
    realism: float
    safety: float
    assessment_value: float
    overall_score: float
    status: Literal["pass", "review", "reject"]
    notes: list[str]
