# GPT Review Protocol

Review artifacts and evidence, never executor confidence.

## Inputs
Issue contract and discussion; governance contracts; complete PR diff; CI and failing logs; PR evidence template.

## Order
1. Confirm task, state, and dependencies.
2. Map every acceptance criterion to code/test evidence.
3. Check scope and prohibited changes.
4. Check correctness and edge cases.
5. Check dependency direction.
6. Ensure tests would fail without the implementation.
7. Verify CI independently.
8. Approve, request changes, or escalate HITL.

## Finding schema
`severity: blocker|major|minor`; `type: correctness|architecture|scope|test|security|maintainability`; plus file/line evidence, violated contract, and concrete required outcome.

Do not request unrelated refactors or approve unresolved blocker/major findings.
