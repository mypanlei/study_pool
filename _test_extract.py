#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script to debug extraction."""

import re
import os

clippings_dir = r"C:\Users\mypan\OneDrive\workspace\study_pool\Clippings"

def is_speaker_line(s):
    s = s.strip()
    if not s or len(s) > 15:
        return False
    for ch in s:
        if not (0x4E00 <= ord(ch) <= 0x9FFF or ch == '-' or ch == '·'):
            return False
    return len(s) >= 2

def is_timestamp_line(s):
    return bool(re.match(r'^\d{1,2}:\d{2}(?::\d{2})?$', s.strip()))

filepath = os.path.join(clippings_dir, "录制文件.md")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove frontmatter
content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
content = re.sub(r'<[^>]+>', '', content)
content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
content = re.sub(r'\[([^\]]*?)\]\(https?://[^\)]+\)', r'\1', content)

lines = content.split('\n')

count = 0
for i, line in enumerate(lines):
    if is_speaker_line(line) and i + 1 < len(lines):
        next_line = lines[i + 1].strip()
        if is_timestamp_line(next_line):
            count += 1
            if count <= 3:
                print(f'Line {i}: speaker=[{line}] ts=[{next_line}]')
                # Show next few lines of dialogue
                j = i + 2
                while j < len(lines) and j < i + 6:
                    print(f'  +{j-i}: [{lines[j].strip()[:60]}]')
                    j += 1
                print()

print(f'Total speaker+timestamp pairs found: {count}')
