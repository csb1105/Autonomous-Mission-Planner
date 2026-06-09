"""
Mission planning orchestration logic.
"""

from typing import List

from mission_planner.config import DEFAULT_ENVIRONMENT_RISK, DEFAULT_RISK_THRESHOLD
from mission_planner.models import (
    Coordinate,
    MissionObjective,
    MissionPlan,
    Platform,
    ThreatZone,
)
from mission_planner.risk import score_route_risk, score_waypoint_risk
from mission_planner.routing import calculate_route_distance_km, generate_basic_route


def validate_constraints(platform: Platform, total_distance_km: float, risk_score: float) -> List[str]:
    violations = []

    if total_distance_km > platform.max_range_km:
        violations.append("Route exceeds platform maximum range.")

    if risk_score > DEFAULT_RISK_THRESHOLD:
        violations.append("Route exceeds default mission risk threshold.")

    return violations


def create_mission_plan(
    mission_id: str,
    platform: Platform,
    start: Coordinate,
    recovery: Coordinate,
    objectives: List[MissionObjective],
    threat_zones: List[ThreatZone],
    environment_risk: float = DEFAULT_ENVIRONMENT_RISK,
) -> MissionPlan:
    waypoints = generate_basic_route(start, recovery, objectives)

    for waypoint in waypoints:
        waypoint.risk_score = score_waypoint_risk(
            waypoint,
            threat_zones,
            environment_risk,
        )

    total_distance_km = round(calculate_route_distance_km(waypoints), 2)
    risk_score = score_route_risk(waypoints, threat_zones, environment_risk)

    constraint_violations = validate_constraints(
        platform,
        total_distance_km,
        risk_score,
    )

    feasible = len(constraint_violations) == 0

    return MissionPlan(
        mission_id=mission_id,
        platform=platform,
        waypoints=waypoints,
        total_distance_km=total_distance_km,
        risk_score=risk_score,
        feasible=feasible,
        constraint_violations=constraint_violations,
        replanning_required=not feasible,
    )
