"""
Reproducible Keyword-Frequency and Rhetorical Density Analysis
Scans the longitudinal raw transcript `02-raw-transcripts/2026-08-14.md`
and computes occurrences of rhetorical/grand keywords across 20-entry windows.
"""
import os
import re

def analyze_keywords(journal_path="02-raw-transcripts/2026-08-14.md"):
    if not os.path.exists(journal_path):
        journal_path = "../02-raw-transcripts/2026-08-14.md"
    if not os.path.exists(journal_path):
        print(f"[-] Journal file not found at {journal_path}")
        return

    print(f"[*] Analyzing rhetorical keyword frequencies in: {journal_path}")
    
    with open(journal_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    keywords = [
        "100%",
        "Grand Seal",
        "終極",
        "大憲章",
        "戰役",
        "無條件證明",
        "突破",
        "完全證明"
    ]
    
    total_counts = {}
    for kw in keywords:
        matches = len(re.findall(re.escape(kw), content, re.IGNORECASE))
        total_counts[kw] = matches
        print(f"    - '{kw}': {matches} occurrences")
        
    print("\n[+] SUMMARY OF RHETORICAL PHENOMENOLOGY:")
    print(f"    Total documented Grand Seal / 100% claims: {total_counts['100%'] + total_counts['Grand Seal']}")
    print(f"    Total tactical / campaign rhetoric mentions: {total_counts['大憲章'] + total_counts['戰役'] + total_counts['終極']}")
    print("[+] Keyword analysis complete.\n")

if __name__ == "__main__":
    analyze_keywords()
