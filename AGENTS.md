# Agent Operating Contract

These instructions apply to every coding agent in this repository.

## Source of truth
Read in order: assigned GitHub Issue, WORKFLOW.md, ARCHITECTURE.md, this file, then relevant source and tests. Chat history is not authoritative. If an Issue conflicts with repository policy, stop for human review.

## Execution rules
- Work on one Issue per branch and PR.
- Stay inside the Issue scope.
- Add or update tests for changed behavior.
- Run `make check` before completion.
- Open a PR using the template; never push directly to `main` or merge your own PR.
- Prefer the standard library unless the Issue explicitly authorizes a dependency.
- Keep domain logic independent of Click and filesystem traversal.

## Prohibited actions
- Do not weaken or delete tests merely to make CI pass.
- Do not swallow broad exceptions.
- Do not add runtime dependencies, change public CLI behavior or persisted formats, edit governance contracts, or expand scope without approval.

## Stop and escalate when
- acceptance criteria conflict or cannot be tested;
- a runtime dependency, secret, permission, or external service is needed;
- architecture boundaries cannot be respected;
- two repairs for the same cause fail.

A block report must state the decision, options, evidence, trade-offs, and recommendation.
