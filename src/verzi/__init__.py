"""Verzi Health: Medicare DME coverage on the date of service, with receipts."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

__all__ = ["check", "mcp_config", "API", "MCP"]
__version__ = "0.1.0"

API = "https://api.verzi.health"
MCP = "https://mcp.verzi.health"


def check(hcpcs: str, state: str | None = None, dos: str | None = None, timeout: float = 20) -> dict:
    """The public code check for one HCPCS code (no key). `dos` is YYYY-MM-DD.
    Returns the JSON answer as a dict."""
    params = {k: v for k, v in (("state", state), ("dos", dos)) if v}
    url = f"{API}/v1/check/{urllib.parse.quote(hcpcs.strip().upper())}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": f"verzi-python/{__version__}"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.load(resp)


def mcp_config(api_key: str = "YOUR_VERZI_API_KEY") -> dict:
    """The MCP client config for Verzi (Claude, Cursor, ChatGPT and others)."""
    return {"mcpServers": {"verzi": {"url": MCP,
                                     "headers": {"Authorization": f"Bearer {api_key}"}}}}
