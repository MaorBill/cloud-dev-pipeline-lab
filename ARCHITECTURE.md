# Architecture Contract

## Purpose
`jsonl-check` validates newline-delimited JSON and reports deterministic, source-oriented diagnostics. The CLI is a test payload for the cloud development pipeline, not a general data platform.

## Boundaries
- `jsonl_check.cli`: arguments, console I/O, exit-code mapping only.
- `jsonl_check.validation`: parse and validate records; no console I/O.
- `jsonl_check.models`: typed results and diagnostics.
- `jsonl_check.reporting`: pure rendering from result models.
- `jsonl_check.discovery` (when introduced): file discovery only.

Dependencies point inward toward models and validation. Domain modules must not import Click.

## Stable contracts
- Process valid UTF-8 JSONL one physical line at a time.
- Line numbers are one-based; diagnostics preserve source path and line.
- Exit 0: all valid. Exit 1: validation completed with invalid records. Exit 2: invocation or operational failure.
- Output ordering is deterministic.

## Non-goals
Distributed workloads, automatic repair, remote storage, web UI, telemetry, and plugin systems are excluded. Changing a stable contract requires HITL.
