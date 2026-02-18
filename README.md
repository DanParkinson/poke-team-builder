# Pokémon Team Builder & Matchup Analyzer

## Vision

Build a professional data-driven web app that allows users to construct a Pokémon team and analyze its defensive weaknesses, offensive coverage, and improvement opportunities using analytical and performance-optimized techniques.

## Epic 1: Database Foundation

Epic 1 focused on establishing a robust and defensive database infrastructure using DuckDB. The goal was to create a production-ready foundation before implementing any data ingestion logic. This included database initialization, connection abstraction, schema definition, idempotent schema management, and validation checks to ensure structural integrity.

The database layer was designed with separation of concerns, defensive error handling, and full test coverage to ensure reliability before moving into the extraction phase.

### Objectives Achieved

- Persistent DuckDB database file creation
- Centralized and defensive connection abstraction
- Explicit relational schema definition
- Idempotent schema application (safe reruns)
- Optional schema rebuild capability
- Structural validation checks before extraction
- Isolated and reproducible test suite using temporary databases
- Clean orchestration via CLI script
- Linting and formatting enforced via pre-commit hooks

## Epic 2: Populate pokemon table
