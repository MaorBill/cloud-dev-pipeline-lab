# Experiment Protocol

## Question
Can a ticket-driven cloud agent complete software changes with low human active time while preserving control, evidence, and recoverability?

## Constraints
- No local IDE or shell implements feature Issues.
- Durable instructions live in GitHub, not chat memory.
- One Issue maps to one branch and one PR.
- Every merge requires green CI and human approval.

## Metrics per Issue
| Metric | Definition |
|---|---|
| Human active time | Minutes specifying, unblocking, or reviewing |
| Agent runtime | Start to PR-ready wall time |
| Intervention count | Human inputs after the trigger |
| First-pass CI | Whether the first revision passed |
| Repair loops | Distinct CI/review cycles |
| Review findings | Blocker / major / minor |
| Cost | Cursor-reported usage, if visible |

## Designed events
Issue 1 tests normal execution and PR handoff. Issue 2 tests a contract-preserving extension. Issue 3 must exercise HITL before a runtime dependency. Issue 4 tests dependent work and regression safety.

## Failure routing
Missing knowledge -> docs. Repeated procedure ambiguity -> workflow/skill. Deterministic defect -> test/lint/CI. Dangerous action -> permission/hook. Task-state ambiguity -> Issue schema. Architecture choice -> HITL decision record.
