from build_indexes import build


def test_resolve_node_by_id_and_url():
    i=build()["nodes.json"]
    assert i["by_id"]["graphiti-retrieval-relevance"]["title"].startswith("Graphiti Fractal")
    u="https://docs.google.com/document/d/1Z-tjZGi_-2ETkWp3NHsmClZIZ_mC23KAOGvAScXLYGA/edit"
    assert i["by_url"][u]=="graphiti-retrieval-drive-track"


def test_reverse_navigation_preserves_direction_without_inventing_edges():
    indexes=build()
    outgoing=indexes["adjacency.json"]["adjacency"]
    incoming=indexes["reverse_adjacency.json"]["reverse_adjacency"]
    neighbors=indexes["neighbors.json"]["neighbors"]
    source="atlas-research-evidence-directory-github"
    target="graphiti-fm16"
    edge=next(x for x in outgoing[source] if x["to"]==target)
    reverse=next(x for x in incoming[target] if x["from"]==source and x["edge"]==edge["edge"])
    assert reverse["relation"]==edge["relation"]
    assert any(x["node"]==target and x["direction"]=="OUT" and x["edge"]==edge["edge"] for x in neighbors[source])
    assert any(x["node"]==source and x["direction"]=="IN" and x["edge"]==edge["edge"] for x in neighbors[target])


def test_index_build_is_deterministic():
    assert build()==build()
