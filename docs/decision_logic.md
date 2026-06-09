# Decision Logic

## Overview

The Autonomous Mission Planner evaluates mission objectives, operational constraints, threat exposure, and environmental conditions to generate a mission recommendation.

The objective is not simply to generate a route, but to generate a route that remains feasible and operationally acceptable.

---

## Decision Pipeline

```text
Mission Input
      |
      v
Platform Validation
      |
      v
Objective Evaluation
      |
      v
Route Generation
      |
      v
Risk Assessment
      |
      v
Constraint Validation
      |
      v
Mission Recommendation
```

---

## Platform Validation

The planner first evaluates platform limitations.

Examples include:

- Maximum range
- Endurance
- Sensor range

Any route exceeding platform limitations is flagged.

---

## Objective Evaluation

Mission objectives are evaluated according to priority.

Higher-priority objectives are considered first during route generation.

Current implementation uses objective priority ordering.

---

## Risk Assessment

The planner evaluates:

- Threat proximity
- Threat severity
- Environmental risk

These values are combined to generate waypoint and route-level risk scores.

---

## Constraint Validation

Mission recommendations are checked against:

- Platform range limits
- Risk thresholds
- Mission feasibility requirements

Constraint violations are recorded within the mission plan.

---

## Mission Recommendation

The final recommendation includes:

- Ordered route
- Route distance
- Risk score
- Feasibility assessment
- Replanning recommendation

---

## Explainability

Every mission recommendation should be traceable to:

- Mission objectives
- Platform constraints
- Threat exposure
- Environmental conditions

The planner is intentionally designed to support explainable autonomy.
