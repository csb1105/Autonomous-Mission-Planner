# Replanning Logic

## Overview

The replanning logic determines whether a mission plan should be reconsidered based on feasibility and operational risk.

The current implementation uses rule-based decision thresholds to keep mission recommendations transparent and explainable.

## Replanning Triggers

A mission should be reconsidered when any of the following conditions occur:

- Route exceeds platform maximum range
- Route exceeds acceptable mission risk threshold
- Mission plan becomes infeasible
- Route risk score exceeds the high-risk threshold

## Current Decision Logic

```text
IF mission is infeasible
    REPLAN

ELSE IF risk score >= high-risk threshold
    REPLAN

ELSE
    CONTINUE MISSION
```

## Risk Thresholds

The current planner uses configurable thresholds defined in:

```text
mission_planner/config.py
```

Example values:

```python
DEFAULT_RISK_THRESHOLD = 0.65
HIGH_RISK_THRESHOLD = 0.85
```

## Operational Interpretation

Replanning does not automatically indicate mission failure.

Instead, replanning indicates that mission conditions have changed enough that the current plan should be reevaluated before continuing execution.

## Future Replanning Capabilities

Future versions may support:

- Dynamic threat updates
- In-flight route adjustment
- Objective reprioritization
- Alternate route comparison
- Human approval gates
- Multi-platform coordination
- Weather-driven replanning
- Sensor-driven replanning

## Design Philosophy

The replanning engine is designed to support human-machine decision making.

The system should not only identify when a mission plan is no longer optimal, but also explain why a different plan is recommended.
