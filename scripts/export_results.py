#!/usr/bin/env python3
"""
⚠️ Disclaimer:
For educational and authorized use only.
------------------------------------------------------------
Script: export_results.py
Purpose: Save queries into a CSV file for reporting.
"""

import csv

# Example queries
dorks = [
    'filetype:pdf "confidential" site:[TARGET]',
    'intitle:"login" site:[TARGET]',
    'filetype:env "DB_PASSWORD" site:[TARGET]'
]

with open("dorks_export.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Query"])
    for dork in dorks:
        writer.writerow([dork])

print("✅ Exported queries to dorks_export.csv")
