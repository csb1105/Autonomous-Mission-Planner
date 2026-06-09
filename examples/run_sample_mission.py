"""
Run a sample mission using the Autonomous Mission Planner.
"""

import json
from pathlib import Path

from mission_planner.models import (
    Coordinate,
    MissionObjective,
    Platform,
    ThreatZone,
)
from mission_planner.planner import create_mission_plan
from mission_planner.simulator import summarize_plan


def load_mission_file(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_platform(data: dict) -> Platform:
    return Platform(
        name=data["name"],
        max_range_km=data["max_range_km"],
        endurance_minutes=data["endurance_minutes"],
        sensor_range_km=data["sensor_range_km"],
    )


def build_objectives(data: list) -> list[MissionObjective]:
    objectives = []

    for item in data:
        objectives.append(
            MissionObjective(
                id=item["id"],
                type=item["type"],
                priority=item["priority"],
                location=Coordinate(
                    lat=item["lat"],
                    lon=item["lon"],
                ),
            )
        )

    return objectives


def build_threat_zones(data: list) -> list[ThreatZone]:
    threat_zones = []

    for item in data:
        threat_zones.append(
            ThreatZone(
                id=item["id"],
                location=Coordinate(
                    lat=item["lat"],
                    lon=item["lon"],
                ),
                radius_km=item["radius_km"],
                severity=item["severity"],
            )
        )

    return threat_zones


def main() -> None:
    mission_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "sample_mission.json"
    )

    mission_data = load_mission_file(mission_file)

    platform = build_platform(mission_data["platform"])

    start = Coordinate(
        lat=mission_data["start"]["lat"],
        lon=mission_data["start"]["lon"],
    )

    recovery = Coordinate(
        lat=mission_data["recovery"]["lat"],
        lon=mission_data["recovery"]["lon"],
    )

    objectives = build_objectives(
        mission_data["objectives"]
    )

    threat_zones = build_threat_zones(
        mission_data["threat_zones"]
    )

    environment_risk = mission_data.get(
        "environment",
        {},
    ).get(
        "risk_factor",
        0.10,
    )

    mission_plan = create_mission_plan(
        mission_id=mission_data["mission_id"],
        platform=platform,
        start=start,
        recovery=recovery,
        objectives=objectives,
        threat_zones=threat_zones,
        environment_risk=environment_risk,
    )

    print("=" * 60)
    print("AUTONOMOUS MISSION PLANNER")
    print("=" * 60)
    print()
    print(summarize_plan(mission_plan))
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
