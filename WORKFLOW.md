# Cloud Development Workflow

## State model
`draft -> ready -> implementing -> human-review -> done`; exceptional states are `blocked` and `cancelled`. Only an Issue marked **State: ready** may start.

## Ready definition
A ready Issue has one measurable goal, explicit scope/non-scope, acceptance criteria, verification, architecture constraints, HITL triggers, and resolved dependencies.

## Executor protocol
1. Read the Issue and governance files.
2. Create `issue-<number>-<slug>`.
3. Inspect the smallest relevant surface.
4. Implement only the contract.
5. Add tests and run `make check`.
6. Open a PR with `Closes #<number>` and complete the evidence template.
7. Stop at human review; never merge.

## Verification gate
Acceptance satisfied + CI green + scope and architecture respected + reviewer approval = merge eligible. Agent confidence is not evidence.

## Repair policy
Fix each distinct CI or review cause once. After two failed repairs for the same cause, mark blocked and request HITL.

## HITL boundaries
Stop before adding a runtime dependency; changing stable CLI/output contracts or architecture; weakening a quality gate; accessing secrets/services; or editing governance policy during a feature task. Provide options, trade-offs, evidence, and recommendation.

## Review severity
Blocker: correctness/security/data loss/policy breach. Major: acceptance or architecture gap, material missing test. Minor: bounded maintainability issue. Blocker and major prevent approval.
