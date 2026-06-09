# Limitations

## Overview

Autonomous Mission Planner is a simulation and portfolio project intended to demonstrate mission-level autonomy concepts.

The project is not designed for operational deployment.

---

## Current Limitations

### Simplified Routing

Routes are currently generated using objective priority ordering.

The planner does not yet perform advanced path optimization or obstacle avoidance.

### Simplified Threat Modeling

Threat zones are represented using circular risk regions and severity values.

Real-world threat analysis would require significantly more sophisticated modeling.

### Static Environment

Environmental conditions are represented by a fixed risk factor.

Dynamic weather, terrain, and operational conditions are not currently modeled.

### Single Platform

The current implementation supports a single unmanned platform.

Multi-platform coordination is planned for future versions.

### Rule-Based Replanning

Replanning decisions currently use configurable threshold logic.

Future versions may include adaptive decision-making approaches.

---

## Not Intended For

This project is not intended for:

- Real-world vehicle control
- Operational mission execution
- Targeting systems
- Weapon systems
- Safety-critical applications
- Flight-certified autonomy

---

## Future Enhancements

Planned improvements include:

- Threat-aware route optimization
- Dynamic replanning
- Sensor coverage analysis
- Multi-platform mission planning
- Environmental modeling
- Advanced autonomy algorithms
