#!/usr/bin/env python3
"""Direct stdio MCP client for xiaohongshu-mcp"""
import subprocess
import json
import sys

def call_tool(tool_name, args=None):
    if args is None:
        args = {}
    
    # Start the MCP server process
    proc = subprocess.Popen(
        ['npx', '-y', 'xiaohongshu-mcp'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Initialize
    init_msg = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "xhs-client", "version": "1.0"}
        }
    }
    proc.stdin.write(json.dumps(init_msg) + '\n')
    proc.stdin.flush()
    
    # Read init response
    init_resp = proc.stdout.readline()
    
    # Send initialized notification
    notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
    proc.stdin.write(json.dumps(notif) + '\n')
    proc.stdin.flush()
    
    # Call the tool
    call_msg = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": args}
    }
    proc.stdin.write(json.dumps(call_msg) + '\n')
    proc.stdin.flush()
    
    # Read tool response
    result = proc.stdout.readline()
    
    # Close
    proc.stdin.close()
    proc.terminate()
    
    try:
        resp = json.loads(result)
        if 'result' in resp and 'content' in resp['result']:
            for c in resp['result']['content']:
                if c.get('type') == 'text':
                    print(c['text'])
                elif c.get('type') == 'image':
                    # Save base64 image
                    import base64
                    data = c.get('data', '')
                    if data:
                        with open('/home/ubuntu/.openclaw/workspace/xhs_qr_latest.png', 'wb') as f:
                            f.write(base64.b64decode(data))
                        print(f"QR code saved to /home/ubuntu/.openclaw/workspace/xhs_qr_latest.png")
        else:
            print(json.dumps(resp, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(f"Raw response: {result}")

if __name__ == '__main__':
    tool = sys.argv[1] if len(sys.argv) > 1 else 'check_login_status'
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    call_tool(tool, args)
