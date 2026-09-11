# 🧭📥 External Research Intake Protocol

**Status:** `DOCUMENTED_CONVENTION · DOCS-ONLY · NO RUNTIME AUTHORITY`  
**Scope:** external projects, repositories, papers, forum posts, tools, systems, mechanisms, and donor ideas proposed for Velantrim research.  
**Origin:** bounded Scout donor review, Knowledge Tree issue #3.  
**Date:** 2026-09-11

## 0. Purpose

This protocol prevents external research from turning into duplicate work, issue floods, silent architecture promotion, or loss of prior disposition history.

It standardizes one narrow workflow:

```text
EXTERNAL SOURCE
      ↓
DISCOVER
      ↓
NORMALIZE IDENTITY
      ↓
DEDUP / CLASSIFY KNOWN STATE
      ↓
RESEARCH CANDIDATE
      ↓
ROUTE TO OWNER PROJECT(S)
      ↓
BOUNDED REVIEW
      ↓
REFERENCE / DONOR / REJECT / DEFER / SUPERSEDE
```

This document is a routing and research-intake convention. It is **not** a runtime subsystem, shared truth ledger, Canon authority, automatic issue generator, or architecture-admission mechanism.

## 1. Non-conflation firewall

```text
DISCOVERED != USEFUL
USEFUL != DONOR
DONOR != ADMITTED
ADMITTED_REFERENCE != ARCHITECTURE
ROUTED != OWNED
SEEN != VERIFIED
DEDUPLICATED != TRUE
REJECTED != DELETED
NEGATIVE KNOWLEDGE != TRUTH
PAST FAILURE != CURRENT IMPOSSIBILITY
AUTOMATION != AUTHORIZATION
RESEARCH != RUNTIME
SPEC != IMPLEMENTATION
IMPLEMENTATION != ACTIVATION
TESTED != PRODUCTION AUTHORIZED
```

A surfaced external source creates, at most, a **research candidate**.

## 2. Stage A — Discover

Record only enough information to identify why the source surfaced.

Minimum discovery fields:

- source title / repository / system name;
- canonical URL or stable identifier;
- source type: repository, paper, forum post, documentation, product, benchmark, other;
- observed date;
- discovery reason / query / user prompt;
- short neutral description;
- possible Velantrim relevance, explicitly marked provisional.

Do not open implementation work merely because the source looks promising.

## 3. Stage B — Normalize identity

Before creating a new research record, normalize the external source identity.

Prefer, in order:

1. canonical repository URL or publication identifier;
2. canonical project/product name;
3. stable upstream organization/owner;
4. alternate aliases only as secondary metadata.

The goal is to recognize the same donor when it appears through different URLs, mirrors, forum posts, or discussion threads.

```text
NEW LINK != NEW SYSTEM
NEW POST != NEW DONOR
NEW DISCUSSION != NEW RESEARCH THREAD BY DEFAULT
```

## 4. Stage C — Dedup and classify known state

Search the Knowledge Tree, Plan & Proposal, owning project issues/research docs, and relevant historical records before creating new work.

Use a reasoned disposition, not a single `seen=true` boolean.

Recommended vocabulary:

- `ALREADY_RESEARCHED`
- `ALREADY_REJECTED`
- `DONOR_CANDIDATE_EXISTS`
- `ISSUE_CANDIDATE_EXISTS`
- `ADMITTED_AS_REFERENCE`
- `SUPERSEDED`
- `DUPLICATE_OF_EXISTING_PROPOSAL`
- `DEFERRED`
- `NEW_CANDIDATE`

These are **research-workflow dispositions**, not truth states.

If an earlier rejection exists, read its scope, evidence, date, applicability conditions, and reopen condition before reusing it.

## 5. Stage D — Create one normalized research candidate

When the source is genuinely new or materially changed, create one primary candidate record.

Minimum candidate record:

- normalized external identity;
- source URL(s);
- observed date;
- why it surfaced;
- current disposition;
- provisional project relevance;
- provenance / evidence references;
- linked prior candidate or rejection if any;
- owner-routing targets;
- current uncertainty / unresolved question.

Do **not** create one independent primary record per project. One external source may route to several owners, but its external identity should remain normalized and cross-linked.

## 6. Stage E — Route to owner projects

Route only where there is a concrete owner-specific question.

Examples:

- 💠 Crystal — evidence, provenance, trusted-memory admission, rejection/supersession history;
- 🌎 Continuum — durable process/task continuity, state transfer, rehydration;
- 🗿 Titan — orchestration, providers, tools, capability/permission boundaries;
- 🧬 Native Kernel — substrate-neutral semantic obligations/invariants;
- 🌀 Mentaury Soul — beliefs, claims, self/identity, cognitive revision;
- 🪁 Mentaury-Kernel — cross-domain semantic composition and authority preservation;
- 🚀 Cognitive OS — LLM-era implementation/routing/evaluation profile;
- ⚗️ CLOS — research-first cognitive blueprint questions;
- 🕸 Graphiti Fractal — memory/retrieval experiments only when the donor actually bears on retrieval/storage/graph behavior;
- 🧭 Knowledge Tree / Atlas / Crosswalk — navigation, relation, and reopen-path questions only.

Do not route to a project for symmetry.

```text
ONE DONOR != ONE ISSUE IN EVERY PROJECT
PROJECT RELEVANCE MUST BE QUESTION-SPECIFIC
```

## 7. Stage F — Bounded owner review

Every owner review should have:

1. one primary research question;
2. explicit non-goals;
3. current live-source check;
4. existing Velantrim mechanism comparison;
5. donor-specific evidence;
6. counterexample / falsification question;
7. one bounded exit verdict;
8. explicit authorization boundary.

Preferred verdict forms:

- already expressible / existing invariants sufficient;
- documentation or consistency gap;
- application pattern only;
- bounded experiment candidate;
- useful reference / negative control;
- not useful;
- deferred pending evidence.

Do not force every review into adoption vs rejection.

## 8. Stage G — Final disposition

A completed candidate should end in one explicit state with reason and provenance.

Possible dispositions:

- `REFERENCE`
- `DONOR_PATTERN`
- `NEGATIVE_CONTROL_REFERENCE`
- `DOC_CONVENTION_GAP`
- `APPLICATION_PATTERN_ONLY`
- `BOUNDED_EXPERIMENT_CANDIDATE`
- `DEFERRED`
- `REJECTED`
- `SUPERSEDED`
- `NOT_USEFUL`

A disposition should preserve:

- scope;
- reason;
- evidence refs;
- established/reviewed date;
- applicability conditions;
- reopen condition where useful;
- superseded-by link where applicable;
- owner/domain.

The exact storage shape belongs to the owning surface. This protocol does not introduce a new mandatory schema.

## 9. Negative knowledge and reopening

Past negative results must remain discoverable without becoming timeless truth.

```text
NEGATIVE KNOWLEDGE != FALSE
REJECTED != FORBIDDEN FOREVER
PAST FAILURE != CURRENT IMPOSSIBILITY
REJECTION RECORD != CANON
REOPEN CONDITION != AUTOMATIC RE-ADMISSION
```

Reopen only when new evidence materially changes at least one of:

- source implementation/version;
- Velantrim requirement;
- prior assumption;
- available evidence;
- owner question;
- applicability conditions.

Do not reopen because the same source was rediscovered.

## 10. Backpressure rule

External discovery must remain cheaper than downstream owner review.

The Scout incident in which a broad discovery pass generated roughly 1,255 mostly noisy candidate issues is retained as a negative-control lesson:

```text
HIGH RECALL DISCOVERY != QUALIFIED INTAKE
CANDIDATE GENERATION != QUALIFICATION
```

Therefore:

- discovery must not automatically create one issue per surfaced result;
- dedup/classification happens before owner work creation;
- owner work is created only for concrete project-specific questions;
- large candidate sets should be triaged in batches before issue creation;
- a retracted/noisy batch should remain traceable rather than silently erased.

## 11. Automation boundary

This protocol does not authorize automation.

If automated discovery is ever added, the safe conceptual sequence is:

```text
SCHEDULE / USER REQUEST
        ↓
READ / DISCOVER / NORMALIZE
        ↓
DRY-RUN CANDIDATE SET
        ↓
QUALIFICATION / DEDUP
        ↓
EXPLICIT AUTHORIZATION FOR MUTATION
        ↓
CREATE / UPDATE OWNER RECORDS
        ↓
RECEIPT / TRACE
```

```text
CAPABILITY != PERMISSION
PREVIEW != APPLY
RECEIPT != AUTHORIZATION
```

Any automation or mutation path requires a separate owner decision and belongs to the appropriate runtime/orchestration owner, not to the Knowledge Tree itself.

## 12. Source-role discipline

Use the existing Velantrim source hierarchy.

- **Plan & Proposal:** external idea/donor intake and long-form proposal context.
- **Knowledge Tree:** discoverability, relations, owner routes, reopen paths.
- **Crosswalk:** cross-project semantic relationships and first-hop routing.
- **Atlas:** global orientation/navigation.
- **Owning GitHub/Notion/Drive surfaces:** project-specific truth, current status, evidence, and history according to their established roles.

```text
TREE != OWNER
CROSSWALK != OWNER
ATLAS != OWNER
ROUTING != ADMISSION
```

## 13. Minimal operator checklist

Before creating new research work for an external source, answer:

- What exact external object is this?
- Have we seen/researched/rejected/deferred it before?
- Is there materially new evidence?
- Which owner question does it create?
- Why does that owner need a separate review?
- What is the smallest bounded question?
- What evidence would falsify the donor's usefulness?
- What explicit verdict will close the review?
- What is **not** authorized by this review?

If these questions cannot be answered, keep the source as an unqualified candidate rather than opening implementation work.

## 14. Validation examples

Before considering this convention stable enough for automation, test it manually against at least three cases:

### Case A — genuinely new donor

Expected: normalized candidate → bounded owner route → explicit disposition.

### Case B — already researched donor

Expected: dedup to prior record; no duplicate owner issue unless materially new evidence changes the question.

### Case C — rejected or deferred donor

Expected: prior disposition is recovered with reason/evidence/reopen condition; rediscovery alone does not revive it.

Success means the process preserves discoverability and prior reasoning **without** turning the Knowledge Tree into a truth database or creating duplicate work.

## 15. Authority statement

This protocol is documentation only.

It does not authorize:

- new runtime components;
- a shared candidate database;
- automatic GitHub issue creation;
- automatic donor admission;
- Canon writes;
- architecture promotion;
- production integration;
- Graphiti retrieval changes;
- Titan mutation-policy changes;
- Continuum Pilot/Evidence Lock changes.

Any such step requires its own bounded owner decision and evidence.

---

**Research provenance:** Daily-Nerd/scout bounded donor audit; Knowledge Tree #3; Crystal #479; Continuum #54; Titan #456; Native Kernel #188; Graphiti Fractal Lab #1.
