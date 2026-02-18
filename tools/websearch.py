#!/usr/bin/env python3
"""Headless web search using Playwright."""

import sys
import json
from playwright.sync_api import sync_playwright

def search_duckduckgo(query: str, max_results: int = 10) -> list[dict]:
    """Search DuckDuckGo and return results."""
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Use the HTML-only version (more stable)
        page.goto(f"https://html.duckduckgo.com/html/?q={query}")
        page.wait_for_selector(".result", timeout=15000)
        
        # Extract results
        items = page.query_selector_all(".result")
        
        for item in items[:max_results]:
            try:
                title_el = item.query_selector(".result__a")
                snippet_el = item.query_selector(".result__snippet")
                
                if title_el:
                    results.append({
                        "title": title_el.inner_text(),
                        "url": title_el.get_attribute("href"),
                        "snippet": snippet_el.inner_text() if snippet_el else ""
                    })
            except:
                continue
        
        browser.close()
    
    return results

def search_google(query: str, max_results: int = 10) -> list[dict]:
    """Search Google and return results."""
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        page.goto(f"https://www.google.com/search?q={query}")
        page.wait_for_selector("#search", timeout=15000)
        
        items = page.query_selector_all("#search .g")
        
        for item in items[:max_results]:
            try:
                title_el = item.query_selector("h3")
                link_el = item.query_selector("a")
                snippet_el = item.query_selector("[data-sncf], .VwiC3b")
                
                if title_el and link_el:
                    url = link_el.get_attribute("href")
                    if url and url.startswith("http"):
                        results.append({
                            "title": title_el.inner_text(),
                            "url": url,
                            "snippet": snippet_el.inner_text() if snippet_el else ""
                        })
            except:
                continue
        
        browser.close()
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: websearch.py <query> [engine] [max_results]")
        print("  engine: duckduckgo (default) or google")
        sys.exit(1)
    
    query = sys.argv[1]
    engine = sys.argv[2] if len(sys.argv) > 2 else "duckduckgo"
    max_results = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    
    if engine == "google":
        results = search_google(query, max_results)
    else:
        results = search_duckduckgo(query, max_results)
    
    print(json.dumps(results, indent=2))
