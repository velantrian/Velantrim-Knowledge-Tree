from __future__ import annotations
import sys
from urllib.parse import urlparse
from _tree import load_nodes
def main():
    errors=[]; checked=0
    for n in load_nodes():
        u=n.get("url")
        if not u: continue
        checked+=1; p=urlparse(u)
        if p.scheme not in {"http","https"} or not p.netloc: errors.append(f"{n['id']}: malformed URL {u}")
    if errors:
        for e in errors: print("ERROR:",e)
        return 1
    print(f"PASS: {checked} URLs syntactically valid; remote/auth availability intentionally not asserted"); return 0
if __name__=="__main__": sys.exit(main())
