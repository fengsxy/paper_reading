#!/usr/bin/env python3
"""
Xiaohongshu API client using your cookies
"""
import requests
import json
import os
import time
import hashlib
import random
import string

COOKIES_PATH = os.path.expanduser('~/.xiaohongshu/cookies.json')

class XhsClient:
    def __init__(self, cookies_path=COOKIES_PATH):
        with open(cookies_path) as f:
            self.cookies_dict = json.load(f)
        
        self.session = requests.Session()
        for k, v in self.cookies_dict.items():
            self.session.cookies.set(k, v, domain='.xiaohongshu.com')
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.xiaohongshu.com/',
            'Origin': 'https://www.xiaohongshu.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
    
    def check_login(self):
        """Check if logged in by accessing creator center"""
        resp = self.session.get(
            'https://creator.xiaohongshu.com/creator/home',
            headers=self.headers,
            allow_redirects=False
        )
        if resp.status_code == 200:
            return True, "已登录"
        elif resp.status_code == 302:
            loc = resp.headers.get('Location', '')
            if 'login' in loc.lower():
                return False, "未登录 (重定向到登录页)"
            return False, f"重定向到: {loc}"
        return False, f"状态码: {resp.status_code}"
    
    def get_user_info(self):
        """Get current user info from creator center"""
        resp = self.session.get(
            'https://creator.xiaohongshu.com/api/galaxy/creator/home/personal_info',
            headers=self.headers
        )
        return resp.json()
    
    def search_notes(self, keyword, page=1, page_size=20):
        """Search notes by keyword"""
        # This requires X-S signature which is complex
        # For now, return a placeholder
        return {"error": "Search requires X-S signature generation"}
    
    def get_note_detail(self, note_id, xsec_token=None):
        """Get note detail by ID"""
        # This also requires signature
        return {"error": "Note detail requires X-S signature generation"}

def main():
    import sys
    client = XhsClient()
    
    if len(sys.argv) < 2:
        print("Usage: xhs_client.py <command> [args]")
        print("Commands: check_login, user_info")
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'check_login':
        ok, msg = client.check_login()
        print(f"{'✅' if ok else '❌'} {msg}")
    
    elif cmd == 'user_info':
        info = client.get_user_info()
        print(json.dumps(info, indent=2, ensure_ascii=False))
    
    else:
        print(f"Unknown command: {cmd}")

if __name__ == '__main__':
    main()
