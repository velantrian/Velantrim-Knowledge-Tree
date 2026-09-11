from __future__ import annotations

from collections import Counter, defaultdict, deque
import json
import sys

from _tree import load_edges, load_nodes

ROOT_IDS = {"velantrim", "atlas", "knowledge-tree-github", "graphiti-retrieval-relevance"}
PROJECTISH = {"ECOSYSTEM", "DOMAIN", "PROJECT"}
RESEARCH_TYPES = {"RESEARCH_THREAD", "EXPERIMENT"}
HISTORICAL_STATES = {"ARCHIVED", "SUPERSEDED", "DEPRECATED"}
RETURN_RELATIONS = {"ROUTES_TO", "BELONGS_TO", "RELATED_TO", "SUPERSEDED_BY", "LED_TO"}


def bfs(start: str, adjacency: dict[str, list[str]]) -> set[str]:
    seen = {start}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for nxt in adjacency.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def main() -> int:
    nodes = load_nodes()
    edges = load_edges()
    by_id = {n["id"]: n for n in nodes}

    outgoing: dict[str, list[dict]] = defaultdict(list)
    incoming: dict[str, list[dict]] = defaultdict(list)
    out_ids: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        outgoing[e["from"]].append(e)
        incoming[e["to"]].append(e)
        out_ids[e["from"]].append(e["to"])

    orphans = [n for n in nodes if not outgoing[n["id"]] and not incoming[n["id"]]]
    sinks = [n for n in nodes if not outgoing[n["id"]]]
    incoming_only = [n for n in sinks if incoming[n["id"]]]
    primary_sinks = [n for n in sinks if n.get("reopen_priority") == "PRIMARY"]

    reachable_from_velantrim = bfs("velantrim", out_ids) if "velantrim" in by_id else set()
    not_reachable_from_velantrim = [n for n in nodes if n["id"] not in reachable_from_velantrim]

    can_reach_root = []
    cannot_reach_root = []
    for n in nodes:
        reached = bfs(n["id"], out_ids)
        (can_reach_root if reached & ROOT_IDS else cannot_reach_root).append(n)

    broken_reopen_refs = []
    open_research_without_reopen = []
    for n in nodes:
        research = n.get("research") or {}
        refs = research.get("next_reopen_path") or []
        for ref in refs:
            if ref not in by_id:
                broken_reopen_refs.append((n["id"], ref))
        if n["type"] in RESEARCH_TYPES and n["status"] in {"OPEN", "CURRENT", "DRAFT"}:
            if research and not refs:
                open_research_without_reopen.append(n)

    historical_without_successor = []
    for n in nodes:
        is_hist = n.get("historical") is True or n["status"] in HISTORICAL_STATES or n["maturity"] in {"HISTORICAL", "ARCHIVED", "SUPERSEDED"}
        if not is_hist:
            continue
        has_field = bool(n.get("superseded_by"))
        has_edge = any(e["relation"] in {"SUPERSEDED_BY", "LED_TO", "ROUTES_TO"} for e in outgoing[n["id"]])
        if not has_field and not has_edge:
            historical_without_successor.append(n)

    project_missing_direct_status = []
    project_missing_repo = []
    for n in nodes:
        if n["type"] not in PROJECTISH:
            continue
        outs = outgoing[n["id"]]
        if not any(e["relation"] == "HAS_CURRENT_STATE" for e in outs):
            project_missing_direct_status.append(n)
        if n["type"] == "PROJECT" and not any(
            e["relation"] in {"HAS_PRODUCT_REPO", "HAS_LAB_REPO"}
            or (e["relation"] == "HAS_GITHUB_DOC" and by_id.get(e["to"], {}).get("type") == "REPOSITORY")
            for e in outs
        ):
            project_missing_repo.append(n)

    return_edge_sources = []
    for n in incoming_only:
        # A leaf with only incoming edges cannot execute AGENTS.md's one-known-node -> expand-one-hop path
        # using the current directed adjacency index.
        return_edge_sources.append(n)

    summary = {
        "nodes": len(nodes),
        "edges": len(edges),
        "orphans": len(orphans),
        "sinks": len(sinks),
        "incoming_only_sinks": len(incoming_only),
        "primary_sinks": len(primary_sinks),
        "not_reachable_from_velantrim_outgoing": len(not_reachable_from_velantrim),
        "cannot_reach_any_root_outgoing": len(cannot_reach_root),
        "broken_next_reopen_refs": len(broken_reopen_refs),
        "open_research_without_next_reopen_path": len(open_research_without_reopen),
        "historical_without_successor_route": len(historical_without_successor),
        "projectish_without_direct_current_state": len(project_missing_direct_status),
        "projects_without_direct_repo_route": len(project_missing_repo),
    }

    print("BATCH8_NAVIGATION_GAP_AUDIT")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print()
    print("SINKS_BY_TYPE", json.dumps(Counter(n["type"] for n in sinks), sort_keys=True))
    print("PRIMARY_SINKS_BY_TYPE", json.dumps(Counter(n["type"] for n in primary_sinks), sort_keys=True))
    print()

    def show(label: str, items, limit: int = 30):
        print(label)
        if not items:
            print("  NONE")
            return
        for item in items[:limit]:
            if isinstance(item, tuple):
                print("  " + " -> ".join(item))
            else:
                print(f"  {item['id']} | {item['type']} | {item['status']} | {item['title']}")
        if len(items) > limit:
            print(f"  ... +{len(items)-limit} more")

    show("ORPHANS", orphans)
    show("PRIMARY_SINKS", primary_sinks)
    show("BROKEN_NEXT_REOPEN_REFS", broken_reopen_refs)
    show("OPEN_RESEARCH_WITHOUT_NEXT_REOPEN_PATH", open_research_without_reopen)
    show("HISTORICAL_WITHOUT_SUCCESSOR_ROUTE", historical_without_successor)
    show("PROJECTISH_WITHOUT_DIRECT_CURRENT_STATE", project_missing_direct_status)
    show("PROJECTS_WITHOUT_DIRECT_REPO_ROUTE", project_missing_repo)
    show("EXAMPLES_INCOMING_ONLY_SINKS", return_edge_sources, limit=40)

    print()
    print("INTERPRETATION")
    print("  incoming_only_sinks are not automatically bad data nodes; many are legitimate leaf sources.")
    print("  They are a navigation gap only for the documented AGENTS.md behavior: INPUT one known node -> expand one hop.")
    print("  Current indexes/adjacency.json stores outgoing edges only, so a leaf source cannot discover its owning context without reverse lookup.")
    print("  Recommended bounded repair: preserve directed adjacency and add deterministic reverse_adjacency/neighbors indexes; do not invent reciprocal authority edges.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
