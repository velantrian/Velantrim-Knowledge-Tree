# Relation Types

Edges are typed and carry a human-readable `description` explaining **why** the relation exists.

Allowed relations include `OWNS`, `BELONGS_TO`, `DOCUMENTS`, `IMPLEMENTS`, `TESTS`, `VALIDATES`, `EXPLAINS`, `SUMMARIZES`, `HAS_CURRENT_STATE`, `HAS_HISTORY`, `HAS_REASONING_LOG`, `HAS_EXECUTABLE_EVIDENCE`, `HAS_RESEARCH`, `HAS_ARTIFACT`, `HAS_DISCUSSION_HISTORY`, `HAS_PROPOSAL`, `RELATED_TO`, `DERIVED_FROM`, `LED_TO`, `SUPERSEDES`, `SUPERSEDED_BY`, `CONTRADICTS`, `CLARIFIES`, `REVIEWS`, `ROUTES_TO`, `REFERENCES`, `HAS_PRODUCT_REPO`, `HAS_LAB_REPO`, `HAS_NOTION_PAGE`, `HAS_DRIVE_DOC`, `HAS_GITHUB_DOC`, `HAS_ISSUE`, `HAS_PR`, `HAS_COMMIT`, `HAS_TESTS`.

Prefer the most precise relation available. Generic `RELATED_TO` requires a meaningful explanatory description.
