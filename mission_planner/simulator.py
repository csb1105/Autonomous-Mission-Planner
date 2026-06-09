"""
Mission simulation helpers.
"""

from mission_planner.config import HIGH_RISK_THRESHOLD
from mission_planner.models import MissionPlan


def should_replan(plan: MissionPlan) -> bool:
    if not plan.feasible:
        return True

    if plan.risk_score >= HIGH_RISK_THRESHOLD:
        return True

    return False


def summarize_plan(plan: MissionPlan) -> str:
    waypoint_sequence = " -> ".join(waypoint.id for waypoint in plan.waypoints)

    violations = (
        "None"
        if not plan.constraint_violations
        else "; ".join(plan.constraint_violations)
    )

    return (
        f"Mission ID: {plan.mission_id}\n"
        f"Platform: {plan.platform.name}\n"
        f"Selected Route: {waypoint_sequence}\n"
        f"Total Distance: {plan.total_distance_km} km\n"
        f"Risk Score: {plan.risk_score}\n"
        f"Mission Feasible: {plan.feasible}\n"
        f"Constraint Violations: {violations}\n"
        f"Replanning Required: {should_replan(plan)}"
    )
