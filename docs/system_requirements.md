# System Requirements

## Overview

The Autonomous Mission Planner is designed to run as a lightweight Python application.

---

## Software Requirements

### Python

```text
Python 3.11+
```

### Dependencies

Installed through:

```bash
pip install -r requirements.txt
```

Current dependencies:

- numpy
- pandas
- matplotlib
- pydantic
- pytest

---

## Operating Systems

Supported environments include:

- macOS
- Linux
- Windows

---

## Repository Structure Requirements

The repository expects the following directories:

```text
data/
examples/
mission_planner/
tests/
docs/
```

---

## Runtime Requirements

The application requires:

- Mission input JSON file
- Platform definition
- Mission objectives
- Threat zone definitions

---

## Visualization Requirements

Mission visualization requires:

```text
matplotlib
```

The visualization module displays:

- Mission route
- Waypoints
- Threat zones

---

## CI/CD Requirements

GitHub Actions is used to execute:

- Automated tests
- Dependency installation
- Continuous validation

---

## Design Goal

The project is intentionally lightweight to simplify experimentation, demonstration, and educational use.
