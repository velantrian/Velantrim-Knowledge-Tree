# 🤖 AGENTS.md — Velantrim Knowledge Tree

This repository is a **navigation graph**, not a truth authority.

## Required reading behavior

1. Resolve the exact node by ID, URL, title, repository name, Drive document ID, or Notion page ID.
2. Read `why_read`, `authoritative_for`, and `not_authoritative_for` before following links.
3. Expand only the relations relevant to the user's question.
4. Open the underlying owning source before making substantive claims.
5. Re-check volatile GitHub claims against the live repository/ref.
6. Use Google Drive for long-form rationale, discussion history, research evolution, and rejected alternatives.
7. Use Notion for human-readable current status, owning project hubs, governance, and quick routes.
8. Use exact GitHub code/tests/artifacts/commits for executable evidence.
9. Never promote a research node into implementation, runtime, Canon, or product authority.
10. Preserve `UNKNOWN`; do not infer absence from an inaccessible or unindexed source.

## Minimal routing algorithm

```text
INPUT: one known node
  ↓
resolve exact node
  ↓
read role + authority boundaries
  ↓
expand one hop
  ↓
rank relations by current question
  ↓
open required underlying source
  ↓
verify evidence
  ↓
answer
```

## Non-conflation firewall

```text
RESEARCH ≠ RUNTIME
SPEC ≠ IMPLEMENTATION
IMPLEMENTATION ≠ ACTIVATION
TESTED ≠ PRODUCTION AUTHORIZED
RETRIEVAL ≠ EVIDENCE
EVIDENCE ≠ BELIEF
BELIEF ≠ TRUTH
CAPABILITY ≠ PERMISSION
MODEL OUTPUT ≠ CANON
UNKNOWN ≠ FALSE
NOT RETRIEVED ≠ ABSENT
ATLAS ≠ OWNER
KNOWLEDGE TREE ≠ OWNER
CROSSWALK ≠ ATLAS
LAB ≠ PRODUCT
DISCUSSION ≠ EXECUTABLE EVIDENCE
SUMMARY ≠ SOURCE
```
