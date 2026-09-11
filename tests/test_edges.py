from _tree import load_edges,load_nodes
def test_no_dangling_edges():
    ids={n["id"] for n in load_nodes()}
    for e in load_edges(): assert e["from"] in ids and e["to"] in ids and e["from"]!=e["to"]
def test_every_edge_has_explanatory_description():
    for e in load_edges(): assert len(e["description"].strip())>=12
