# 🌳🧭 Batch 8 — Navigation Gap / Reopen-Path Audit

Date: 2026-09-11

Mode: bounded structural audit · evidence-first · no authority promotion · no runtime activation

## Purpose

Batch 8 did not add another broad population wave. It tested whether the existing Knowledge Tree can actually be reopened from an arbitrary known node, especially a leaf/source node, without the original chat.

The governing requirement comes from `AGENTS.md`:

```text
INPUT: one known node
  → resolve exact node
  → read role + authority boundaries
  → expand one hop
  → open underlying source
  → verify evidence
```

The audit therefore distinguishes **semantic graph direction** from **navigation lookup direction**.

```text
EDGE DIRECTION = MEANING
NAVIGATION LOOKUP = DISCOVERY AID

REVERSE LOOKUP ≠ REVERSED CLAIM
INCOMING EDGE ≠ RECIPROCAL SEMANTIC EDGE
NEIGHBORHOOD ≠ AUTHORITY TRANSFER
```

## Baseline before repair

Frozen Batch-7 baseline:

```text
159 nodes
225 typed edges
144 syntactically valid URLs
11 tests
```

Initial Batch-8 diagnostic found:

```text
orphans                              = 0
broken next_reopen_path refs         = 0
incoming-only sinks                  = 94
PRIMARY sinks                        = 86
not reachable from Velantrim OUT     = 1
historical without successor route   = 1
open research without metadata path  = 2
project/domain warnings: no direct
HAS_CURRENT_STATE                    = 4
projects without repo route          = 0
```

## Finding A — the main structural navigation gap

The Tree's semantic edges are intentionally directed, usually from owner/context toward source/evidence. That is correct for meaning, but the generated `indexes/adjacency.json` contained only outgoing edges.

As a result, a reader who begins from a leaf source can know the source node but cannot discover the incoming owner/research context through the generated adjacency index alone.

This is not evidence that 94 source nodes are malformed. Most are legitimate terminal evidence/doc/status nodes.

The gap is instead:

```text
SEMANTICALLY VALID LEAF
        +
OUTGOING-ONLY LOOKUP
        ↓
ONE-NODE REOPEN CAN STALL
```

### Bounded repair

`build_indexes.py` now preserves the original directed `adjacency.json` and additionally generates:

- `reverse_adjacency.json` — incoming-edge lookup;
- `neighbors.json` — bidirectional navigation projection carrying the original `edge`, `relation`, and `direction: IN|OUT`.

No reciprocal semantic edges are invented.

A regression test verifies that the Atlas Research Evidence Directory → Graphiti FM-16 `ROUTES_TO` edge is represented with the same edge ID and relation in outgoing, incoming, and neighborhood projections while preserving direction.

`AGENTS.md` now tells an AI to use these indexes when the starting node is a leaf/source.

## Finding B — one genuinely unreachable historical Graphiti source

Initial outgoing traversal from `velantrim` reached 158/159 nodes. The sole missing node was:

`graphiti-retrieval-track-pre-fm16-summary`

This source is intentionally historical/superseded. It remains useful for FM-13→FM-15 and pre-FM-16 protocol history, but its stale current-frontier text must not be used as current truth.

### Bounded repair

Added:

```text
graphiti-retrieval-relevance
  --HAS_HISTORY-->
graphiti-retrieval-track-pre-fm16-summary
```

After repair:

```text
not_reachable_from_velantrim_outgoing = 0
```

The repair makes history discoverable without promoting the historical snapshot.

## Finding C — Native Kernel historical D7 lacked a forward current-state route

The archived node `native-kernel-bpv1-d7-rereview-github` explicitly explains scoped historical strengthening, but the audit found no outgoing successor/current route.

That is risky when a future AI enters through the historical document directly: the text itself says current routing must continue through the present project state/H11 gate.

### Bounded repair

Added:

```text
native-kernel-bpv1-d7-rereview-github
  --ROUTES_TO-->
native-kernel-project-state-github
```

After repair:

```text
historical_without_successor_route = 0
```

This preserves:

```text
HISTORICAL BPV1 EVIDENCE ≠ CURRENT H11 GATE
HISTORICAL REVIEW ≠ FINAL CANON
HISTORICAL REVIEW ≠ RUNTIME THAW
```

## Warnings that were deliberately NOT auto-repaired

Two current research nodes have research metadata but no explicit `research.next_reopen_path` array:

- Titan — Execution Observation & Evaluation Contract;
- Mentaury Soul — Cognitive Orientation View v0.1.

Both already have meaningful graph routes. Therefore this is treated as **metadata completeness**, not proof of a broken navigation path. Batch 8 does not duplicate routes merely to make a metric zero.

Four project/domain-level nodes lack a direct `HAS_CURRENT_STATE` edge:

- `velantrim`;
- `graphiti-fractal`;
- `cognitive-os`;
- `living-culture`.

This is also retained as a review warning. Some project/domain nodes intentionally route via repository, Notion, product/lab, or other owner surfaces. No direct current-state edge is invented without owner evidence.

The large count of nodes that cannot reach a root using **outgoing semantic edges only** is likewise not treated as a defect. In an owner→source directed graph, many leaves should not semantically point back to roots. Reverse/neighborhood indexes solve navigation without corrupting edge meaning.

## Post-repair executable result

Fresh Batch-8 validation after the two evidence-backed graph repairs and index regeneration:

```text
PASS: 159 nodes, 227 edges
PASS: deterministic indexes up to date
PASS: 144 URLs syntactically valid
      remote/auth availability intentionally not asserted
PASS: 12 tests

orphans                              = 0
broken next_reopen_path refs         = 0
not reachable from Velantrim OUT     = 0
historical without successor route   = 0
incoming-only sinks                  = 93
open research metadata warnings      = 2
project/domain current-state warnings= 4
projects without repo route          = 0
```

## What Batch 8 establishes

Batch 8 establishes a bounded navigation capability:

```text
KNOWN LEAF SOURCE
      ↓
resolve exact node
      ↓
inspect original authority boundaries
      ↓
OUT edges + IN lookup projection
      ↓
recover owner / research / history neighborhood
      ↓
open deeper owning source
      ↓
verify before claim
```

It does **not** establish semantic retrieval, autonomous graph reasoning, current-truth inference, authority inheritance, or runtime activation.

## Preserved firewall

```text
NAVIGATION ≠ AUTHORITY
REVERSE LOOKUP ≠ REVERSED CLAIM
NEIGHBOR ≠ OWNER
EDGE EXISTS ≠ SOURCE VERIFIED
CURRENT LABEL ≠ CURRENT TRUTH WITHOUT RECHECK
HISTORICAL ≠ CURRENT
RESEARCH ≠ RUNTIME
IMPLEMENTATION ≠ ACTIVATION
```

## Current bounded conclusion

The most important Batch-8 defect was not missing project content. It was that the machine index could descend from context to sources much better than it could reopen context from a known leaf source.

That asymmetry is now repaired at the **index/navigation layer**, not by falsifying the semantic graph with reciprocal edges.
