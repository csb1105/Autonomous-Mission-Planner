"""
Basic mission visualization utilities.
"""

from typing import List

import matplotlib.pyplot as plt

from mission_planner.models import ThreatZone, Waypoint


def plot_mission_route(waypoints: List[Waypoint], threat_zones: List[ThreatZone]) -> None:
    waypoint_lats = [waypoint.location.lat for waypoint in waypoints]
    waypoint_lons = [waypoint.location.lon for waypoint in waypoints]

    plt.figure(figsize=(8, 6))
    plt.plot(waypoint_lons, waypoint_lats, marker="o", label="Mission Route")

    for waypoint in waypoints:
        plt.text(waypoint.location.lon, waypoint.location.lat, waypoint.id)

    for threat in threat_zones:
        plt.scatter(
            threat.location.lon,
            threat.location.lat,
            s=threat.radius_km * 40,
            alpha=0.3,
            label=f"Threat Zone: {threat.id}",
        )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Autonomous Mission Plan")
    plt.legend()
    plt.grid(True)
    plt.show()
