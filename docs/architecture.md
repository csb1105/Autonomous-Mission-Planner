# Architecture

## System Purpose

Autonomous Mission Planner is organized as a mission-level autonomy simulation framework. It models how an unmanned system can evaluate objectives, constraints, threats, and environmental conditions before generating a risk-aware mission plan.

The system is not designed as a low-level flight controller. It operates at the planning and decision-support layer.

## Core Components

### Mission Planning Engine

**Location:** `mission_planner/planner.py`

**Responsibilities:**

- Accept mission objectives
- Load platform constraints
- Coordinate route generation
- Apply risk scoring
- Validate mission feasibility
- Return the final mission plan

### Routing Engine

**Location:** `mission_planner/routing.py`

**Responsibilities:**

- Create waypoint sequences
- Order objectives by priority
- Calculate route distance
- Support future alternate route generation

### Risk Engine

**Location:** `mission_planner/risk.py`

**Responsibilities:**

- Score waypoint risk
- Score route-level risk
- Evaluate threat-zone proximity
- Apply environmental risk factors

### Simulation Layer

**Location:** `mission_planner/simulator.py`

**Responsibilities:**

- Summarize mission plans
- Identify replanning conditions
- Support future mission-state updates

### Visualization Layer

**Location:** `mission_planner/visualization.py`

**Responsibilities:**

- Plot mission waypoints
- Display threat zones
- Support human review of mission plans

## Data Flow

```text
Mission JSON
    |
    v
Data Models
    |
    v
Route Generation
    |
    v
Risk Scoring
    |
    v
Constraint Validation
    |
    v
Mission Plan
    |
    v
Simulation Summary
    |
    v
Visualization
```

## Design Principle

The project is structured to demonstrate explainable autonomy. Each planning decision should be traceable to mission objectives, platform limits, threat exposure, or environmental conditions.
