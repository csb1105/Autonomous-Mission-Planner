# Sample Mission Output

## Example Scenario

Mission ID:

```text
MISSION-001
```

Platform:

```text
UAS-Alpha
```

Objectives:

```text
OBJ-1
OBJ-2
```

Threat Zones:

```text
THREAT-1
THREAT-2
```

---

## Example Planner Output

```text
============================================================
AUTONOMOUS MISSION PLANNER
============================================================

Mission ID: MISSION-001

Platform: UAS-Alpha

Selected Route:
START -> OBJ-1 -> OBJ-2 -> RECOVERY

Total Distance:
22.41 km

Risk Score:
0.53

Mission Feasible:
True

Constraint Violations:
None

Replanning Required:
False

============================================================
```

---

## Interpretation

The planner successfully generated a feasible route that:

- Visits all objectives
- Remains within platform constraints
- Maintains acceptable risk levels
- Does not require replanning

This output is intended to provide a human-readable explanation of mission recommendations.
