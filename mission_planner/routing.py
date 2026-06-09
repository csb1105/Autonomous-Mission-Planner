"""
Route generation and distance calculations.
"""

from math import radians, sin, cos, sqrt, atan2
from typing import List

from mission_planner.config import EARTH_RADIUS_KM
from mission_planner.models import Coordinate, MissionObjective, Waypoint


def haversine_distance_km(point_a: Coordinate, point_b: Coordinate) -> float:
    lat1 = radians(point_a.lat)
    lon1 = radians(point_a.lon)
    lat2 = radians(point_b.lat)
    lon2 = radians(point_b.lon)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c


def calculate_route_distance_km(waypoints: List[Waypoint]) -> float:
    total = 0.0

    for index in range(len(waypoints) - 1):
        total += haversine_distance_km(
            waypoints[index].location,
            waypoints[index + 1].location,
        )

    return total


def generate_basic_route(
    start: Coordinate,
    recovery: Coordinate,
    objectives: List[MissionObjective],
) -> List[Waypoint]:
    ordered_objectives = sorted(objectives, key=lambda obj: obj.priority)

    waypoints = [
        Waypoint(id="START", location=start, task_type="launch")
    ]

    for objective in ordered_objectives:
        waypoints.append(
            Waypoint(
                id=objective.id,
                location=objective.location,
                task_type=objective.type,
            )
        )

    waypoints.append(
        Waypoint(id="RECOVERY", location=recovery, task_type="recovery")
    )

    return waypoints
