# verzi

A small Python client for [Verzi Health](https://verzi.health): Medicare durable
medical equipment (DME) coverage on the date of service, with receipts.

```
pip install verzi
```

## Check a code (no key needed)

```python
import verzi

answer = verzi.check("E0601", state="UT", dos="2023-12-20")
print(answer["coverage"]["summary"])
print(answer["governing"]["lcds"])
```

From the command line:

```
verzi check E0601 --state UT --dos 2023-12-20
```

The public check names the LCD CMS lists for the code, the CMS source citation,
and how many documentation requirements Verzi serves. The signed receipt
(standing, fee, edits and documentation, each pinned to its source) needs a
paid plan: see https://docs.verzi.health.

## Connect an AI agent (MCP)

```
verzi mcp-config
```

prints the config for an MCP client such as Claude, Cursor or ChatGPT. The
server is `https://mcp.verzi.health`. Get a free key at
https://api.verzi.health/signup.

Verzi serves CMS's own words. It is a receipt for the published rule, not a
guarantee of payment or medical necessity.
