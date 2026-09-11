from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
NODE_DIR = ROOT / "registry" / "nodes"
EDGE_DIR = ROOT / "registry" / "edges"
def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f: return json.load(f)
def load_nodes():
    nodes=[]
    for path in sorted(NODE_DIR.glob("*.json")): nodes.extend(load_json(path).get("nodes", []))
    return nodes
def load_edges():
    edges=[]
    for path in sorted(EDGE_DIR.glob("*.json")): edges.extend(load_json(path).get("edges", []))
    return edges
def canonical_json(data): return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)+"\n"
