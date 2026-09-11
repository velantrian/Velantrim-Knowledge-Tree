from build_indexes import build
def test_resolve_node_by_id_and_url():
    i=build()["nodes.json"]; assert i["by_id"]["graphiti-retrieval-relevance"]["title"].startswith("Graphiti Fractal"); u="https://docs.google.com/document/d/1Z-tjZGi_-2ETkWp3NHsmClZIZ_mC23KAOGvAScXLYGA/edit"; assert i["by_url"][u]=="graphiti-retrieval-drive-track"
def test_index_build_is_deterministic(): assert build()==build()
