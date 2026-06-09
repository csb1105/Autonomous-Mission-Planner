# Architecture

## System Purpose

Autonomous Mission Planner is organized as a mission-level autonomy simulation framework. It models how an unmanned system can evaluate objectives, constraints, threats, and environmental conditions before generating a risk-aware mission plan.

The system is not designed as a low-level flight controller. It operates at the planning and decision-support layer.

## Core Components

## Mission Planning Engine

Located in:

```text
mission_planner/planner.py
