#!/usr/bin/env python3
"""Direct stdio MCP client for xiaohongshu-mcp"""
import subprocess
import json
import sys

def list_tools():
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
    print("Init:", init_resp.strip())
    
    # Send initialized notification
    notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
    proc.stdin.write(json.dumps(notif) + '\n')
    proc.stdin.flush()
    
    # List tools
    list_msg = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }
    proc.stdin.write(json.dumps(list_msg) + '\n')
    proc.stdin.flush()
    
    # Read response
    result = proc.stdout.readline()
    
    # Close
    proc.stdin.close()
    proc.terminate()
    
    try:
        resp = json.loads(result)
        if 'result' in resp and 'tools' in resp['result']:
            print("\nAvailable tools:")
            for t in resp['result']['tools']:
                print(f"  - {t['name']}: {t.get('description', '')[:60]}")
        else:
            print(json.dumps(resp, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(f"Raw response: {result}")

if __name__ == '__main__':
    list_tools()
