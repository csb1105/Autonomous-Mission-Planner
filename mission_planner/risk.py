"""
Risk scoring logic for mission routes.
"""

from typing import List

from mission_planner.config import DEFAULT_ENVIRONMENT_RISK, RISK_WEIGHTS
from mission_planner.models import ThreatZone, Waypoint
from mission_planner.routing import haversine_distance_km


def score_waypoint_risk(
    waypoint: Waypoint,
    threat_zones: List[ThreatZone],
    environment_risk: float = DEFAULT_ENVIRONMENT_RISK,
) -> float:
    if not threat_zones:
        return environment_risk

    highest_threat_score = 0.0

    for threat in threat_zones:
        distance = haversine_distance_km(waypoint.location, threat.location)

        if distance <= threat.radius_km:
            proximity_score = 1.0
        else:
            proximity_score = max(0.0, 1.0 - ((distance - threat.radius_km) / threat.radius_km))

        threat_score = (
            RISK_WEIGHTS["threat_proximity"] * proximity_score
            + RISK_WEIGHTS["threat_severity"] * threat.severity
            + RISK_WEIGHTS["environment"] * environment_risk
        )

        highest_threat_score = max(highest_threat_score, threat_score)

    return round(min(highest_threat_score, 1.0), 3)


def score_route_risk(
    waypoints: List[Waypoint],
    threat_zones: List[ThreatZone],
    environment_risk: float = DEFAULT_ENVIRONMENT_RISK,
) -> float:
    if not waypoints:
        return 0.0

    waypoint_scores = [
        score_waypoint_risk(waypoint, threat_zones, environment_risk)
        for waypoint in waypoints
    ]

    return round(sum(waypoint_scores) / len(waypoint_scores), 3)
