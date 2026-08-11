from adaptive_cyber_risk_training import LearnerProfile, ScenarioGenerator, ScenarioQualityAssurance
from adaptive_cyber_risk_training.evaluation import engagement_summary, skill_transfer_index


def test_generated_scenario_passes_quality_gate():
    profile = LearnerProfile(
        learner_id="test_001",
        level="beginner",
        target_skill="likelihood and impact reasoning",
    )
    scenario = ScenarioGenerator().generate(profile)
    report = ScenarioQualityAssurance().score(scenario)
    assert report.status == "pass"
    assert report.safety == 1.0
    assert report.overall_score >= 0.82


def test_evaluation_helpers_return_normalized_scores():
    assert skill_transfer_index(0.45, 0.70, 0.80) == 0.47
    assert engagement_summary(0.80, 0.70, 0.90) == 0.8
