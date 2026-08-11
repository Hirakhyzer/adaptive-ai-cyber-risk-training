from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adaptive_cyber_risk_training import LearnerProfile, ScenarioGenerator, ScenarioQualityAssurance


profile = LearnerProfile(
    learner_id="learner_001",
    level="intermediate",
    target_skill="residual risk justification",
    prior_errors=["missed business impact", "weak control evaluation"],
)

scenario = ScenarioGenerator().generate(profile, sector="healthcare")
report = ScenarioQualityAssurance().score(scenario)

print("Scenario ID:", scenario.scenario_id)
print("Learning objective:", scenario.learning_objective)
print("QA status:", report.status)
print("Overall score:", report.overall_score)
print("Notes:")
for note in report.notes:
    print("-", note)
