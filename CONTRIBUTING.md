# Contributing

## Project Status

Autonomous Mission Planner is a portfolio and demonstration repository focused on mission-level autonomy concepts.

The project emphasizes:

- Mission planning
- Risk-aware decision support
- Operational constraints
- Human-machine teaming
- Explainable autonomy

## Development Principles

Contributions should follow these principles:

- Keep autonomy logic explainable.
- Prefer readable Python over unnecessary complexity.
- Preserve modular architecture.
- Keep mission planning tied to operational constraints.
- Maintain clear separation between routing, risk, planning, simulation, and visualization.

## Code Style

Recommended practices:

- Use type hints where appropriate.
- Keep functions focused and readable.
- Use descriptive variable names.
- Add docstrings to public functions.

## Testing

Run the test suite before committing changes:

```bash
pytest
```

## Appropriate Future Enhancements

Examples of acceptable enhancements include:

- Alternate route generation
- Threat-aware route optimization
- Environmental risk modeling
- Sensor coverage analysis
- Mission replay capabilities
- Multi-platform mission planning

## Out of Scope

The following are intentionally outside the scope of this repository:

- Real-world targeting
- Weapon system control
- Flight-certified autonomy
- Hardware-specific vehicle control
