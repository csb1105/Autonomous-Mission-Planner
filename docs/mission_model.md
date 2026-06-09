# Mission Model

## Overview

The mission model defines the operational inputs used by the Autonomous Mission Planner.

A mission scenario includes:

- Platform constraints
- Start location
- Recovery location
- Mission objectives
- Threat zones
- Environmental risk factors

## Platform

The platform describes the unmanned system assigned to the mission.

Example:

```json
{
  "name": "UAS-Alpha",
  "max_range_km": 120,
  "endurance_minutes": 90,
  "sensor_range_km": 15
}
```

## Mission Objectives

Objectives define the tasks the platform must complete.

Example:

```json
{
  "id": "OBJ-1",
  "type": "surveillance",
  "priority": 1,
  "lat": 34.05,
  "lon": -117.04
}
```

Lower priority numbers represent higher-priority mission objectives.

## Threat Zones

Threat zones represent areas of elevated operational risk.

Example:

```json
{
  "id": "THREAT-1",
  "lat": 34.07,
  "lon": -117.06,
  "radius_km": 8,
  "severity": 0.8
}
```

Severity is represented on a scale from `0.0` to `1.0`.

## Environment

The environment object provides a mission-wide risk factor.

Example:

```json
{
  "risk_factor": 0.15
}
```

## Mission Output

The planner produces a mission plan containing:

- Mission ID
- Platform information
- Ordered waypoint sequence
- Total route distance
- Route risk score
- Feasibility assessment
- Constraint violations
- Replanning status

## Sample Mission Structure

```text
Mission
├── Platform
├── Start Location
├── Recovery Location
├── Objectives
├── Threat Zones
└── Environment
```
