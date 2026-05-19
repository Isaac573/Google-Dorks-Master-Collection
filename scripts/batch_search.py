#!/usr/bin/env python3
"""
⚠️ Disclaimer:
For educational and authorised use only.
------------------------------------------------------------
Script: batch_search.py
Purpose: Run multiple queries with a chosen domain filter.
"""

import webbrowser

# Domain filter
domain = "site:[TARGET]"

# Batch queries
keywords = ["confidential pdf", "admin login", "database dump"]

for keyword in keywords:
    query = f"{keyword} {domain}"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
