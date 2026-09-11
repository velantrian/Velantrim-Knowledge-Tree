from __future__ import annotations
import argparse, sys
from _tree import ROOT, canonical_json, load_edges, load_nodes
INDEX_DIR=ROOT/"indexes"

def build():
    nodes=sorted(load_nodes(),key=lambda n:n["id"]); edges=sorted(load_edges(),key=lambda e:e["id"])
    by_id={n["id"]:{"title":n["title"],"type":n["type"],"url":n.get("url"),"source_system":n["source_system"]} for n in nodes}
    by_url={n["url"].rstrip("/"):n["id"] for n in nodes if n.get("url")}
    projects={n["id"]:{"title":n["title"],"owner_domain":n["owner_domain"]} for n in nodes if n["type"] in {"PROJECT","ECOSYSTEM"}}
    research={n["id"]:{"title":n["title"],"status":n["status"],"maturity":n["maturity"]} for n in nodes if n["type"] in {"RESEARCH_THREAD","EXPERIMENT"}}
    tags={}; adjacency={}; reverse_adjacency={}; neighbors={}
    for n in nodes:
        for t in n.get("related_tags",[]): tags.setdefault(t,[]).append(n["id"])
    for ids in tags.values(): ids.sort()
    for e in edges:
        adjacency.setdefault(e["from"],[]).append({"edge":e["id"],"to":e["to"],"relation":e["relation"]})
        reverse_adjacency.setdefault(e["to"],[]).append({"edge":e["id"],"from":e["from"],"relation":e["relation"]})
        neighbors.setdefault(e["from"],[]).append({"edge":e["id"],"node":e["to"],"direction":"OUT","relation":e["relation"]})
        neighbors.setdefault(e["to"],[]).append({"edge":e["id"],"node":e["from"],"direction":"IN","relation":e["relation"]})
    for items in adjacency.values(): items.sort(key=lambda x:(x["relation"],x["to"],x["edge"]))
    for items in reverse_adjacency.values(): items.sort(key=lambda x:(x["relation"],x["from"],x["edge"]))
    for items in neighbors.values(): items.sort(key=lambda x:(x["direction"],x["relation"],x["node"],x["edge"]))
    return {
        "nodes.json":{"by_id":by_id,"by_url":by_url},
        "projects.json":{"projects":projects},
        "research.json":{"research":research},
        "tags.json":{"tags":dict(sorted(tags.items()))},
        "adjacency.json":{"adjacency":dict(sorted(adjacency.items()))},
        "reverse_adjacency.json":{"reverse_adjacency":dict(sorted(reverse_adjacency.items()))},
        "neighbors.json":{"neighbors":dict(sorted(neighbors.items()))},
        "roots.json":{"roots":[
            {"id":"velantrim","title":"Velantrim","type":"ECOSYSTEM"},
            {"id":"atlas","title":"Velantrim Knowledge Atlas","type":"DOMAIN"},
            {"id":"knowledge-tree-github","title":"Velantrim Knowledge Tree","type":"REPOSITORY"},
            {"id":"graphiti-retrieval-relevance","title":"Graphiti Fractal — Retrieval Relevance","type":"RESEARCH_THREAD"}
        ]}
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("--check",action="store_true"); args=p.parse_args(); generated=build(); mismatches=[]; INDEX_DIR.mkdir(exist_ok=True)
    for name,data in generated.items():
        text=canonical_json(data); path=INDEX_DIR/name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8")!=text: mismatches.append(name)
        else: path.write_text(text,encoding="utf-8")
    if mismatches: print("INDEX_MISMATCH:",", ".join(mismatches)); return 1
    print("PASS: indexes deterministic and up to date" if args.check else "WROTE: "+", ".join(sorted(generated))); return 0

if __name__=="__main__": sys.exit(main())
