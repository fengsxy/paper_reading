#!/usr/bin/env python3
import requests
import json
import sys

BASE = "http://127.0.0.1:18060/mcp"
session = requests.Session()

# Initialize
init_req = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "openclaw", "version": "1.0"}
    }
}
r = session.post(BASE, json=init_req)
print("Init:", r.json())

# Get session ID from response headers if any
session_id = r.headers.get('mcp-session-id') or r.headers.get('Mcp-Session-Id')
print(f"Session ID: {session_id}")

headers = {}
if session_id:
    headers['mcp-session-id'] = session_id

# Send initialized notification
notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
r = session.post(BASE, json=notif, headers=headers)
print("Notif status:", r.status_code)

# List tools
list_req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
r = session.post(BASE, json=list_req, headers=headers)
print("Tools:", json.dumps(r.json(), indent=2, ensure_ascii=False))

# Check login status
if len(sys.argv) > 1 and sys.argv[1] == "login":
    call_req = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "check_login_status",
            "arguments": {}
        }
    }
    r = session.post(BASE, json=call_req, headers=headers)
    print("Login status:", json.dumps(r.json(), indent=2, ensure_ascii=False))
