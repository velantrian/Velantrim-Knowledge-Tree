from _tree import load_nodes
def test_no_authority_overlap():
    for n in load_nodes(): assert not(set(n["authoritative_for"])&set(n["not_authoritative_for"]))
def test_lab_does_not_claim_product_authorization():
    n=next(n for n in load_nodes() if n["id"]=="graphiti-fractal-lab"); assert "graphiti_product_runtime_authorization" in n["not_authoritative_for"]
