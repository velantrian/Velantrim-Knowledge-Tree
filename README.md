# 🌳🧭 Velantrim Knowledge Tree

**STATUS:** `RESEARCH_NAVIGATION_INFRASTRUCTURE`  
**DATA COMPLETENESS:** `PARTIAL / BOOTSTRAP`  
**RUNTIME:** `NOT_AUTHORIZED`  
**PRODUCTION:** `NOT_AUTHORIZED`  
**CANON AUTHORITY:** `NONE`

Velantrim Knowledge Tree is a machine-readable navigation graph for the Velantrim ecosystem. Give it one known node — a project, repository, document, Notion page, research thread, experiment, issue, PR, artifact, or concept — and use the graph to discover the surrounding knowledge surface.

```text
ONE NODE
   │
   ▼
🌳 KNOWLEDGE TREE
   │
   ├── 📄 Google Drive — history / rationale / long-form discussion
   ├── 📝 Notion — current route / status / owner
   ├── 💻 GitHub — exact code / tests / artifacts / commits
   ├── 🗺️ Atlas — global orientation
   └── 🧭🔀 Crosswalk — cross-project relations
              │
              ▼
          REOPEN SOURCE
              │
              ▼
           CONTINUE
```

## Core law

```text
KNOWLEDGE TREE = NAVIGATION + RELATIONSHIPS + SOURCE DISCOVERY + REOPEN PATHS
KNOWLEDGE TREE ≠ CANON
KNOWLEDGE TREE ≠ RUNTIME
KNOWLEDGE TREE ≠ MEMORY DATABASE
KNOWLEDGE TREE ≠ PROJECT OWNER
```

The tree makes accumulated knowledge **discoverable**. It does not replace the underlying knowledge.

## What it answers

Starting from one node, a future AI or human should be able to answer:

- What is this?
- Which project or research thread does it belong to?
- Where is the current status?
- Where is the long-form history or discussion?
- Where is executable evidence?
- Which other nodes are related?
- Why are they related?
- Which source should be opened next?

## Repository layout

- `registry/nodes/` — curated source and project nodes.
- `registry/edges/` — typed relationships with explanatory comments.
- `schema/` — JSON Schemas for nodes, edges, registry, and exported trees.
- `scripts/validate_tree.py` — structural and semantic-integrity checks.
- `scripts/build_indexes.py` — deterministic lookup indexes.
- `scripts/check_links.py` — URL syntax checks without pretending authenticated sources are absent.
- `indexes/` — generated deterministic lookup material.
- `docs/` — authority model, source roles, update protocol, and reading guidance.
- `examples/` — bounded examples, currently centered on Graphiti Fractal retrieval relevance.

## Source precedence depends on the question

For volatile technical claims:

```text
LIVE EXACT REPOSITORY STATE
> EXECUTABLE ARTIFACTS / TESTS
> EXPERIMENT CODE
> CURRENT STATUS DOC
> NOTION CURRENT PAGE
> DRIVE LONG-FORM NARRATIVE
> KNOWLEDGE TREE SUMMARY
```

For historical reasoning — *why a hypothesis changed, what was rejected, what discussion led to an experiment* — a Drive long-form research document or a GitHub reasoning log may be the primary source.

## Bootstrap content

The repository starts with a curated baseline rather than an indiscriminate crawl. Graphiti Fractal → Retrieval Relevance is the model example because its knowledge already spans:

- Google Drive long-form discussion/history;
- Notion current research navigation;
- GitHub lab code, reasoning log, experiment branch, artifacts, and FM-16 closure;
- explicit product-vs-lab authority boundaries.

Other project roots are present only where the source identity is already known. `PARTIAL TREE ≠ COMPLETE ECOSYSTEM INVENTORY`.

## Validation

```bash
python scripts/validate_tree.py
python scripts/build_indexes.py --check
python scripts/check_links.py
pytest -q
```

See [`AGENTS.md`](AGENTS.md) for AI navigation rules and [`docs/UPDATE_PROTOCOL.md`](docs/UPDATE_PROTOCOL.md) for maintenance discipline.
