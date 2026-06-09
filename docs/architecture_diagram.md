# Architecture Diagram

## System Architecture

```text
+----------------------+
|   Mission Input      |
|----------------------|
| Objectives           |
| Threat Zones         |
| Platform Constraints |
| Environment Data     |
+----------+-----------+
           |
           v
+----------------------+
|   Data Models        |
|----------------------|
| Platform             |
| Objective            |
| Threat Zone          |
| Waypoint             |
| Mission Plan         |
+----------+-----------+
           |
           v
+----------------------+
| Routing Engine       |
|----------------------|
| Route Generation     |
| Distance Calculation |
+----------+-----------+
           |
           v
+----------------------+
| Risk Engine          |
|----------------------|
| Threat Analysis      |
| Risk Scoring         |
+----------+-----------+
           |
           v
+----------------------+
| Mission Planner      |
|----------------------|
| Feasibility Checks   |
| Constraint Validation|
| Plan Generation      |
+----------+-----------+
           |
           v
+----------------------+
| Simulation Layer     |
|----------------------|
| Replanning Logic     |
| Mission Summary      |
+----------+-----------+
           |
           v
+----------------------+
| Visualization Layer  |
|----------------------|
| Route Display        |
| Threat Display       |
+----------------------+
```

## Design Goal

Each layer has a single responsibility and communicates through well-defined mission-planning data structures.
