"""verzi check E0601 [--state UT] [--dos 2023-12-20] | verzi mcp-config"""
from __future__ import annotations

import argparse
import json
import sys

from . import check, mcp_config


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="verzi", description="Verzi Health: Medicare DME coverage on the date of service, with receipts.")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="the public check for one HCPCS code (no key)")
    c.add_argument("hcpcs")
    c.add_argument("--state")
    c.add_argument("--dos", help="date of service, YYYY-MM-DD")
    m = sub.add_parser("mcp-config", help="print the MCP client config")
    m.add_argument("--key", default="YOUR_VERZI_API_KEY")
    a = p.parse_args(argv)
    if a.cmd == "check":
        out = check(a.hcpcs, a.state, a.dos)
    else:
        out = mcp_config(a.key)
    json.dump(out, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
