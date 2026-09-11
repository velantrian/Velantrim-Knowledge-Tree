from __future__ import annotations
import sys
from collections import Counter
from jsonschema import Draft202012Validator
from _tree import ROOT, load_edges, load_json, load_nodes

def validate():
    errors=[]
    node_validator=Draft202012Validator(load_json(ROOT/"schema"/"node.schema.json"))
    edge_validator=Draft202012Validator(load_json(ROOT/"schema"/"edge.schema.json"))
    nodes=load_nodes(); edges=load_edges()
    for n in nodes:
        for e in node_validator.iter_errors(n): errors.append(f"node {n.get('id','?')}: {e.message}")
    for e0 in edges:
        for e in edge_validator.iter_errors(e0): errors.append(f"edge {e0.get('id','?')}: {e.message}")
    node_ids=[n.get("id") for n in nodes]; edge_ids=[e.get("id") for e in edges]
    for value,count in Counter(node_ids).items():
        if count>1: errors.append(f"duplicate node id: {value}")
    for value,count in Counter(edge_ids).items():
        if count>1: errors.append(f"duplicate edge id: {value}")
    ids=set(node_ids); urls={}
    for n in nodes:
        if n.get("url"): urls.setdefault(n["url"].rstrip("/"),[]).append(n["id"])
        overlap=set(n.get("authoritative_for",[])) & set(n.get("not_authoritative_for",[]))
        if overlap: errors.append(f"authority conflict {n['id']}: {sorted(overlap)}")
    for u,v in urls.items():
        if len(v)>1: errors.append(f"duplicate canonical url {u}: {v}")
    for e in edges:
        if e["from"] not in ids: errors.append(f"dangling edge {e['id']} from={e['from']}")
        if e["to"] not in ids: errors.append(f"dangling edge {e['id']} to={e['to']}")
        if e["from"]==e["to"]: errors.append(f"self-edge not allowed: {e['id']}")
    if errors:
        for e in errors: print("ERROR:",e)
        return 1
    print(f"PASS: {len(nodes)} nodes, {len(edges)} edges")
    return 0
if __name__=="__main__": sys.exit(validate())
