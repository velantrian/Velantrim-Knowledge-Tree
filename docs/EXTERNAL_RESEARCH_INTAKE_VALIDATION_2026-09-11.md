# 🧭🧪 External Research Intake Protocol — Manual Validation

**Date:** 2026-09-11  
**Mode:** `DOCS-ONLY · MANUAL VALIDATION · NO AUTO-WRITES · NO ARCHITECTURE PROMOTION`  
**Protocol under test:** `docs/EXTERNAL_RESEARCH_INTAKE_PROTOCOL.md`

## 0. Purpose

Validate the proposed external-research intake convention against real live objects before considering it stable enough for merge or any later automation discussion.

The test is deliberately narrow. It validates routing/dedup/disposition behavior, not runtime automation.

## 1. Pre-test repository hygiene check

The first protocol branch was created from `main@07da1dac7172780722d759de6c205a996c7b0d48`.

Before validation, live `main` had advanced to:

`d5eaf65b9d60b228342d7557102fe61cea69edf9`

The old branch was therefore 14 commits behind current `main` and GitHub reported PR #10 as not mergeable at the time of the fresh check.

Disposition:

`SUPERSEDED_BRANCH_BASE`

Action:

- do not merge the stale branch;
- recreate the same docs-only change from fresh `main`;
- preserve the old PR as historical provenance until the replacement exists;
- no force update and no unrelated rebasing side effects.

This is itself evidence that fresh live-source reconciliation belongs before any final admission/merge decision.

## 2. Case A — genuinely new external candidate

### Source

`https://github.com/techtheist/engram`

Observed focus supplied for intake:

`https://github.com/techtheist/engram/tree/main/eval`

Fresh inspection confirmed a real `eval/` surface containing, among other items:

- `CONTRADICTIONS.md`;
- `LONGMEMEVAL.md`;
- `README.md`;
- `results/`;
- `src/`.

Search across current Velantrim GitHub issues for `techtheist engram` returned no open or closed issue match at validation time.

### Normalized identity

`github:techtheist/engram`

### Intake classification

`NEW_CANDIDATE`

### Provisional routing

Potential bounded owner questions exist for:

- 🕸 Graphiti Fractal — evaluation methodology for memory/retrieval and contradiction-sensitive retrieval experiments;
- 💠 Crystal — contradiction/provenance/evidence-handling comparison if the donor contains concrete mechanisms relevant to Crystal ownership.

No issue is created by this validation because the protocol requires an owner-specific question and bounded donor audit before downstream work creation.

### Result

`PASS`

The protocol successfully distinguishes discovery from admission and permits a real new source to be normalized/routed without immediately multiplying project issues.

```text
DISCOVERED != USEFUL
NEW_CANDIDATE != OWNER ISSUE
PROVISIONAL ROUTE != ADMISSION
```

## 3. Case B — already researched donor

### Source

`https://github.com/Daily-Nerd/scout`

### Existing primary record

Knowledge Tree issue #3:

`🔬 Research intake: Scout-style discovery → dedup → candidate → human admission`

Fresh live check:

- state: `closed`;
- state reason: `completed`;
- one completion comment exists;
- closed at `2026-09-11T14:24:34Z`.

Related owner reviews already exist across Crystal, Continuum, Titan, Native Kernel and Graphiti Fractal.

### Intake classification

`ALREADY_RESEARCHED`

### Required action

- recover issue #3 and its owner-review lineage;
- do not create another primary Scout intake issue;
- reopen only if materially new Scout evidence changes a bounded owner question.

### Result

`PASS`

The protocol deduplicates rediscovery to an existing completed research lineage instead of treating the same donor as new work.

```text
REDISCOVERED != NEW
ALREADY_RESEARCHED != REOPEN
NO NEW EVIDENCE != NO NEW ISSUE
```

## 4. Case C — previously negative/dispositioned duplicate candidate

### Live record

Knowledge Tree issue #4:

`🔬 Research: Scout-style donor discovery → dedup → issue-candidate intake`

Fresh live check:

- state: `closed`;
- state reason: `duplicate`;
- closed at `2026-09-11T12:09:39Z`;
- primary surviving Scout intake is issue #3.

### Intake classification

`DUPLICATE_OF_EXISTING_PROPOSAL`

This is a real negative workflow disposition. It is not a claim that Scout is false, useless, forbidden, or permanently rejected.

### Required action on rediscovery

- keep #4 closed;
- route back to #3;
- preserve #4 as history explaining why a second candidate was not admitted;
- do not delete or silently forget the duplicate;
- do not revive it merely because Scout is encountered again.

### Result

`PASS`

```text
DUPLICATE != USELESS
CLOSED_DUPLICATE != DELETED_HISTORY
REDISCOVERY != REOPEN CONDITION
NEGATIVE DISPOSITION != TRUTH CLAIM
```

### Limitation

This validation used a live `duplicate` disposition because it was the clearest directly verifiable external-intake negative case available in the checked GitHub surfaces. It should not be falsely relabeled `REJECTED` or `DEFERRED`.

A future genuinely rejected/deferred external donor can be used as an additional regression case without changing this protocol.

## 5. Validation summary

| Case | Real object | Expected behavior | Observed protocol outcome |
|---|---|---|---|
| A | `techtheist/engram` | recognize genuinely new candidate without auto-issue flood | `PASS · NEW_CANDIDATE` |
| B | `Daily-Nerd/scout` / KT #3 | recover existing completed lineage | `PASS · ALREADY_RESEARCHED` |
| C | KT #4 duplicate Scout intake | preserve negative disposition; no revival | `PASS · DUPLICATE_OF_EXISTING_PROPOSAL` |

Overall:

`MANUAL_INTAKE_VALIDATION = PASS`

with one explicit limitation:

`REJECTED_OR_DEFERRED_EXTERNAL_DONOR_REGRESSION = NOT_YET_EXECUTED`

## 6. What this validates

Evidence supports the documentation convention for:

- normalized identity;
- duplicate suppression;
- existing-research recovery;
- owner routing without issue multiplication;
- preservation of negative workflow history;
- fresh-base reconciliation before merge;
- explicit non-admission boundaries.

## 7. What this does NOT validate

This manual pass does **not** establish:

- automated discovery quality;
- automatic normalization correctness;
- automatic dedup correctness;
- a shared candidate ledger;
- autonomous GitHub issue creation;
- runtime safety;
- architecture admission;
- Canon authority;
- production readiness.

```text
MANUAL PROTOCOL PASS != AUTOMATION PROOF
THREE CASES != GENERAL CORRECTNESS
DOC VALIDATION != RUNTIME AUTHORIZATION
```

## 8. Bounded verdict

`SAFE_DOCS_ONLY_REVIEW_CANDIDATE = YES`

subject to:

1. replacement PR being based on fresh `main`;
2. exact changed-file audit showing docs-only scope;
3. CI/checks on the replacement exact head succeeding where applicable;
4. no concurrent `main` change creating a new conflict before merge review;
5. no claim that this validation authorizes automation or implementation.

No merge is performed by this validation.
