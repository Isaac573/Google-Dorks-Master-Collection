#!/usr/bin/env python3
"""
⚠️ Disclaimer:
For educational and authorised use only.
Do not use these queries against systems without explicit authorisation.
Always follow responsible disclosure practices.
------------------------------------------------------------
Script: open_dorks.py
Purpose: Automatically open selected Google Dorks in the browser.
"""

import webbrowser

# Example queries
dorks = [
    'filetype:pdf "confidential" site:[TARGET]',
    'intitle:"login" site:[TARGET]',
    'filetype:env "DB_PASSWORD" site:[TARGET]'
]

for query in dorks:
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
