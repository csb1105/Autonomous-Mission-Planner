"""
Core data models for mission planning.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Coordinate:
    lat: float
    lon: float


@dataclass
class Platform:
    name: str
    max_range_km: float
    endurance_minutes: float
    sensor_range_km: float


@dataclass
class MissionObjective:
    id: str
    type: str
    priority: int
    location: Coordinate


@dataclass
class ThreatZone:
    id: str
    location: Coordinate
    radius_km: float
    severity: float


@dataclass
class Waypoint:
    id: str
    location: Coordinate
    task_type: Optional[str] = None
    risk_score: float = 0.0


@dataclass
class MissionPlan:
    mission_id: str
    platform: Platform
    waypoints: List[Waypoint]
    total_distance_km: float
    risk_score: float
    feasible: bool
    constraint_violations: List[str] = field(default_factory=list)
    replanning_required: bool = False
