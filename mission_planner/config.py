"""
Configuration values for the Autonomous Mission Planner.
"""

DEFAULT_RISK_THRESHOLD = 0.65
HIGH_RISK_THRESHOLD = 0.85

RISK_WEIGHTS = {
    "threat_proximity": 0.55,
    "threat_severity": 0.30,
    "environment": 0.15,
}

DEFAULT_ENVIRONMENT_RISK = 0.10

EARTH_RADIUS_KM = 6371.0
