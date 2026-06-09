# Risk Model

## Overview

The Autonomous Mission Planner uses a simplified risk model to evaluate operational exposure during mission planning.

The current implementation is intended for demonstration and educational purposes.

---

## Risk Inputs

Risk calculations consider:

- Threat proximity
- Threat severity
- Environmental risk

Each factor contributes to overall mission risk.

---

## Threat Proximity

Threat proximity measures how close a waypoint is to a known threat zone.

Waypoints located inside a threat zone receive the highest proximity score.

As distance increases, proximity risk decreases.

---

## Threat Severity

Each threat zone contains a severity value.

Example:

```json
{
  "severity": 0.8
}
```

Severity values range from:

```text
0.0 = Minimal Threat
1.0 = Maximum Threat
```

---

## Environmental Risk

Environmental conditions are represented by a mission-wide risk factor.

Example:

```json
{
  "risk_factor": 0.15
}
```

This value represents operational uncertainty not directly associated with known threats.

---

## Route Risk

Route risk is calculated using the average waypoint risk score across the mission route.

Current implementation favors simplicity and explainability.

---

## Risk Thresholds

Default thresholds are defined in:

```text
mission_planner/config.py
```

Example:

```python
DEFAULT_RISK_THRESHOLD = 0.65
HIGH_RISK_THRESHOLD = 0.85
```

---

## Future Improvements

Future versions may include:

- Terrain risk
- Weather risk
- Sensor coverage risk
- Mission exposure analysis
- Dynamic threat intelligence
- Probabilistic risk modeling

---

## Design Goal

The purpose of the risk model is to support mission planning decisions while remaining transparent and explainable to human operators.
