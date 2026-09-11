from _tree import load_edges,load_nodes
def test_node_ids_unique():
    ids=[n["id"] for n in load_nodes()]; assert len(ids)==len(set(ids))
def test_edge_ids_unique():
    ids=[e["id"] for e in load_edges()]; assert len(ids)==len(set(ids))
