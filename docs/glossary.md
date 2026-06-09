# Glossary

## Autonomous Mission Planner

The software framework contained in this repository.

---

## Mission Objective

A task or location that the unmanned system must service during mission execution.

---

## Waypoint

A geographic point included within a mission route.

---

## Route

An ordered sequence of waypoints representing a mission path.

---

## Threat Zone

A geographic region associated with operational risk.

Threat zones are modeled using:

- Location
- Radius
- Severity

---

## Risk Score

A numerical value representing mission exposure to operational risk.

Current values range from:

```text
0.0 = Lowest Risk
1.0 = Highest Risk
```

---

## Platform

The unmanned system assigned to perform the mission.

Example platform constraints include:

- Maximum range
- Endurance
- Sensor range

---

## Mission Plan

The final output produced by the planner.

A mission plan contains:

- Waypoints
- Route distance
- Risk score
- Feasibility status
- Constraint violations
- Replanning recommendations

---

## Replanning

The process of generating a revised mission recommendation when mission conditions exceed acceptable thresholds.

---

## Feasible Mission

A mission that satisfies all platform and risk constraints.

---

## Explainable Autonomy

An autonomy approach where mission recommendations can be traced back to observable inputs, constraints, and decision logic.
