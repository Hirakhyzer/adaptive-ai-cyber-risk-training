from __future__ import annotations

from .schema import CyberRiskScenario, LearnerProfile


class ScenarioGenerator:
    """Template-based adaptive scenario generator.

    This class intentionally avoids offensive procedure generation. It creates
    structured risk-assessment learning cases for defensive education.
    """

    def generate(self, profile: LearnerProfile, sector: str = "healthcare") -> CyberRiskScenario:
        complexity = {
            "beginner": "identify core assets and obvious controls",
            "intermediate": "compare likelihood, impact, and residual risk",
            "advanced": "justify risk treatment across competing business constraints",
        }[profile.level.value]

        return CyberRiskScenario(
            scenario_id=f"adaptive_{profile.learner_id}_{profile.level.value}",
            learner_level=profile.level,
            sector=sector,
            learning_objective=f"Practice cyber risk assessment by learning to {complexity}.",
            asset_context=[
                "identity provider",
                "customer-facing service",
                "backup and recovery process",
            ],
            threat_context="A third-party service dependency introduces uncertainty about availability and data handling.",
            existing_controls=[
                "multi-factor authentication",
                "role-based access control",
                "backup testing",
                "supplier review process",
            ],
            risk_prompt=(
                "Assess likelihood, impact, existing controls, residual risk, and recommend a risk treatment decision. "
                "Keep the answer at organisational risk-assessment level."
            ),
            expected_outputs=[
                "asset identification",
                "threat statement",
                "likelihood rating",
                "impact rating",
                "control evaluation",
                "residual risk justification",
                "treatment recommendation",
            ],
            adaptation_focus=profile.target_skill,
        )
