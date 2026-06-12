#!/usr/bin/env python3
"""Lightweight public-repo safety scan.

This catches common private homelab leaks before publishing. It is intentionally
conservative and should be paired with human review.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SKIP_PARTS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', '.pytest_cache'}
SKIP_NAMES = {'package-lock.json'}
PATTERNS = {
    'private_ip': re.compile(r'\b(?:192\.168|10\.|172\.(?:1[6-9]|2\d|3[01])\.)'),
    'tailscale_ip': re.compile(r'\b100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.'),
    'private_domain': re.compile(r'personaltechwiz\.com|\.local\b', re.I),
    'host_path': re.compile(r'/DATA|/media/devmon|/media/ptw|/mnt/recover|/home/[^/\s]+', re.I),
    'secret_assignment': re.compile(r'(?i)(password|passwd|token|api[_-]?key|secret|passkey)\s*[:=]\s*(?!$|replac|change-me|your-|example|placeholder|\$|\{)[^\s#]+'),
    'long_hex': re.compile(r'(?<![A-Fa-f0-9])[A-Fa-f0-9]{32,}(?![A-Fa-f0-9])'),
}

hits = []
for path in ROOT.rglob('*'):
    if any(part in SKIP_PARTS for part in path.parts) or not path.is_file():
        continue
    rel_path = path.relative_to(ROOT)
    if path.name in SKIP_NAMES or str(rel_path) == 'scripts/public_safety_scan.py':
        continue
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pattern in PATTERNS.items():
            if pattern.search(line):
                hits.append((path.relative_to(ROOT), lineno, name, line.strip()))

if hits:
    for rel, lineno, name, line in hits:
        print(f'{rel}:{lineno} [{name}] {line}')
    sys.exit(2)

print(f'public safety scan clean: {ROOT}')
