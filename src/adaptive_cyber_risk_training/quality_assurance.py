from __future__ import annotations

from statistics import mean

from .schema import CyberRiskScenario, QualityReport


class ScenarioQualityAssurance:
    """Rule-based QA mechanism for adaptive risk-assessment scenarios."""

    prohibited_terms = {
        "payload",
        "exploit code",
        "malware",
        "credential theft",
        "persistence",
        "evasion",
        "exfiltration steps",
    }

    expected_risk_terms = {
        "likelihood",
        "impact",
        "control",
        "residual risk",
        "treatment",
    }

    def score(self, scenario: CyberRiskScenario) -> QualityReport:
        notes: list[str] = []
        text = " ".join(
            [
                scenario.learning_objective,
                scenario.threat_context,
                scenario.risk_prompt,
                scenario.safety_boundary,
                " ".join(scenario.expected_outputs),
            ]
        ).lower()

        safety = 1.0
        found = sorted(term for term in self.prohibited_terms if term in text)
        if found:
            safety = 0.2
            notes.append(f"Unsafe operational terms detected: {', '.join(found)}")
        else:
            notes.append("Safety boundary check passed: scenario remains assessment-focused.")

        correctness = min(1.0, 0.55 + 0.10 * len(scenario.asset_context) + 0.08 * len(scenario.existing_controls))
        consistency = 1.0 if scenario.learner_level.value in scenario.scenario_id else 0.82
        pedagogical_alignment = 0.92 if scenario.adaptation_focus else 0.70
        realism = 0.90 if scenario.sector and len(scenario.asset_context) >= 3 else 0.75
        assessment_value = min(1.0, 0.45 + 0.07 * len(scenario.expected_outputs))

        missing_terms = sorted(term for term in self.expected_risk_terms if term not in text)
        if missing_terms:
            assessment_value = max(0.55, assessment_value - 0.08 * len(missing_terms))
            notes.append(f"Risk-assessment vocabulary missing: {', '.join(missing_terms)}")
        else:
            notes.append("Risk-assessment vocabulary is complete.")

        scores = [correctness, consistency, pedagogical_alignment, realism, safety, assessment_value]
        overall = round(mean(scores), 3)
        status = "pass" if overall >= 0.82 and safety >= 0.80 else "review" if safety >= 0.80 else "reject"

        return QualityReport(
            scenario_id=scenario.scenario_id,
            correctness=round(correctness, 3),
            consistency=round(consistency, 3),
            pedagogical_alignment=round(pedagogical_alignment, 3),
            realism=round(realism, 3),
            safety=round(safety, 3),
            assessment_value=round(assessment_value, 3),
            overall_score=overall,
            status=status,
            notes=notes,
        )
