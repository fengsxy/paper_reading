#!/usr/bin/env python3
import requests
import json
import base64
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
session_id = r.headers.get('mcp-session-id') or r.headers.get('Mcp-Session-Id')
headers = {'mcp-session-id': session_id} if session_id else {}

# Send initialized notification
notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
session.post(BASE, json=notif, headers=headers)

# Get QR code
call_req = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "get_login_qrcode",
        "arguments": {}
    }
}
r = session.post(BASE, json=call_req, headers=headers)
result = r.json()
print(json.dumps(result, indent=2, ensure_ascii=False))

# Extract and save QR image
if 'result' in result and 'content' in result['result']:
    for item in result['result']['content']:
        if item.get('type') == 'image':
            img_data = item.get('data', '')
            if img_data:
                with open('/home/ubuntu/.openclaw/workspace/xhs_qr.png', 'wb') as f:
                    f.write(base64.b64decode(img_data))
                print("\nQR code saved to /home/ubuntu/.openclaw/workspace/xhs_qr.png")
