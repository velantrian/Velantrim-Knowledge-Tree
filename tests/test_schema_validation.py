from jsonschema import Draft202012Validator
from _tree import ROOT,load_edges,load_json,load_nodes
def test_all_nodes_match_schema():
    v=Draft202012Validator(load_json(ROOT/"schema"/"node.schema.json")); assert not [e for n in load_nodes() for e in v.iter_errors(n)]
def test_all_edges_match_schema():
    v=Draft202012Validator(load_json(ROOT/"schema"/"edge.schema.json")); assert not [e for x in load_edges() for e in v.iter_errors(x)]
