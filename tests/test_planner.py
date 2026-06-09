"""
Tests for the Autonomous Mission Planner.
"""

from mission_planner.models import (
    Coordinate,
    MissionObjective,
    Platform,
    ThreatZone,
)
from mission_planner.planner import create_mission_plan


def test_create_mission_plan_returns_feasible_plan():
    platform = Platform(
        name="UAS-Test",
        max_range_km=200,
        endurance_minutes=120,
        sensor_range_km=20,
    )

    start = Coordinate(lat=34.000, lon=-117.000)
    recovery = Coordinate(lat=34.100, lon=-117.100)

    objectives = [
        MissionObjective(
            id="OBJ-1",
            type="surveillance",
            priority=1,
            location=Coordinate(lat=34.050, lon=-117.040),
        )
    ]

    threat_zones = [
        ThreatZone(
            id="THREAT-1",
            location=Coordinate(lat=34.070, lon=-117.060),
            radius_km=5,
            severity=0.5,
        )
    ]

    plan = create_mission_plan(
        mission_id="TEST-MISSION",
        platform=platform,
        start=start,
        recovery=recovery,
        objectives=objectives,
        threat_zones=threat_zones,
        environment_risk=0.1,
    )

    assert plan.mission_id == "TEST-MISSION"
    assert plan.platform.name == "UAS-Test"
    assert len(plan.waypoints) == 3
    assert plan.waypoints[0].id == "START"
    assert plan.waypoints[-1].id == "RECOVERY"
    assert plan.total_distance_km > 0
    assert 0 <= plan.risk_score <= 1
    assert plan.feasible is True


def test_create_mission_plan_flags_range_violation():
    platform = Platform(
        name="UAS-Limited",
        max_range_km=1,
        endurance_minutes=30,
        sensor_range_km=10,
    )

    start = Coordinate(lat=34.000, lon=-117.000)
    recovery = Coordinate(lat=34.100, lon=-117.100)

    objectives = [
        MissionObjective(
            id="OBJ-1",
            type="surveillance",
            priority=1,
            location=Coordinate(lat=34.050, lon=-117.040),
        )
    ]

    plan = create_mission_plan(
        mission_id="RANGE-TEST",
        platform=platform,
        start=start,
        recovery=recovery,
        objectives=objectives,
        threat_zones=[],
        environment_risk=0.1,
    )

    assert plan.feasible is False
    assert "Route exceeds platform maximum range." in plan.constraint_violations
    assert plan.replanning_required is True
