# Cloud Development Pipeline Lab

A controlled experiment for an agent-native cloud workflow. The software is intentionally small: a Python CLI named `jsonl-check`. The experiment is the main product.

## Roles
- Human governor: owns scope, architecture exceptions, dependency decisions, and merge.
- GPT reviewer: creates task contracts and reviews PR diff plus CI evidence.
- Cursor Cloud Agent: implements one ready Issue on a branch and opens a PR.
- GitHub: durable task, code, decision, and audit state.
- GitHub Actions: objective verification gate.

## First run
1. Open Issue #1 and read its complete contract.
2. In Cursor Web, start a Cloud Agent on this repository.
3. Give it the Issue URL plus the trigger prompt from the Issue.
4. Require branch + PR; never direct-push to main.
5. Review CI and artifacts, then merge only if the contract is satisfied.

## Commands
```bash
python -m pip install -e ".[dev]"
make check
python -m jsonl_check --version
```

## Success criteria
State survives session closure; execution resumes from repository artifacts; CI catches deterministic defects; review produces a bounded repair loop; HITL occurs at declared boundaries; the full history is auditable.

Read [WORKFLOW.md](WORKFLOW.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [EXPERIMENT.md](EXPERIMENT.md).
