#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consolidate all recording files from Clippings/ into one deduplicated raw transcript.
"""

import re
import os
import glob

clippings_dir = r"C:\Users\mypan\OneDrive\workspace\study_pool\Clippings"
output_dir = r"C:\Users\mypan\OneDrive\workspace\study_pool\技术经理人中级培训"
output_file = os.path.join(output_dir, "浙江省技术经纪人中级培训-科技成果转化与商业逻辑_raw.md")

files = sorted(glob.glob(os.path.join(clippings_dir, "录制文件*.md")),
               key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group(0)) if re.search(r'\d+', os.path.basename(x)) else 0)

def is_speaker(s):
    s = s.strip()
    if not s or len(s) > 18:
        return False
    for ch in s:
        if not (0x4E00 <= ord(ch) <= 0x9FFF or ch == '-' or ch == '·' or ch == ' '):
            return False
    return len(s) >= 2

def is_ts(s):
    return bool(re.match(r'^\d{1,2}:\d{2}(?::\d{2})?$', s.strip()))

def extract_dialogues(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    # Remove markdown images
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # Remove URLs in text
    content = re.sub(r'https?://\S+', '', content)

    lines = content.split('\n')

    entries = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if is_speaker(line):
            speaker = line
            # Look for timestamp in next few lines (skip blank lines)
            ts_line_idx = None
            for offset in range(1, 4):
                if i + offset < len(lines):
                    nxt = lines[i + offset].strip()
                    if is_ts(nxt):
                        ts_line_idx = i + offset
                        break
                    elif nxt != '':
                        # Non-empty, non-timestamp line - not our pattern
                        break

            if ts_line_idx is not None:
                ts_str = lines[ts_line_idx].strip()
                parts = ts_str.split(':')
                if len(parts) == 3:
                    ts_secs = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
                else:
                    ts_secs = int(parts[0]) * 60 + int(parts[1])

                # Collect dialogue text (skip blank lines after timestamp until next speaker or end marker)
                dialogue = []
                j = ts_line_idx + 1
                while j < len(lines):
                    l = lines[j].strip()
                    if l == '' or l == '定位到正在播放位置':
                        j += 1
                        continue
                    # Check for next speaker
                    if is_speaker(l):
                        # Verify next non-blank line is a timestamp
                        next_text = None
                        for off in range(1, 4):
                            if j + off < len(lines):
                                t = lines[j + off].strip()
                                if t != '':
                                    next_text = t
                                    break
                        if next_text and is_ts(next_text):
                            break
                    dialogue.append(l)
                    j += 1

                text = '\n'.join(dialogue).strip()
                if text:
                    entries.append((speaker, ts_secs, ts_str, text))

                i = j
                continue

        i += 1

    return entries


# Extract all
all_entries = []
for f in files:
    basename = os.path.basename(f)
    entries = extract_dialogues(f)
    print(f"  {basename}: {len(entries)} entries")
    all_entries.extend(entries)

print(f"\nTotal before dedup: {len(all_entries)}")

# Sort by timestamp, then speaker
all_entries.sort(key=lambda x: (x[1], x[0]))

# Dedup: keep first of each (speaker, timestamp_secs)
seen = set()
deduped = []
for speaker, ts_secs, ts_str, text in all_entries:
    key = (speaker, ts_secs)
    if key not in seen:
        seen.add(key)
        deduped.append((speaker, ts_secs, text))

print(f"After dedup: {len(deduped)}")

# Write output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("---\n")
    f.write("title: 浙江省技术经纪人中级培训 - 会议文字记录（整合去重）\n")
    f.write("created: 2026-06-17\n")
    f.write("tags:\n")
    f.write("  - 技术经理人\n")
    f.write("  - 中级培训\n")
    f.write("  - 会议记录\n")
    f.write("  - raw\n")
    f.write("---\n\n")
    f.write("# 浙江省技术经纪人中级培训 - 会议文字记录\n\n")
    f.write("来源：腾讯会议录制\n\n")
    f.write("日期：2026-06-17\n\n")
    f.write("时长：2:33:13\n\n")
    f.write("---\n\n")

    prev_speaker = None
    for speaker, ts_secs, text in deduped:
        h = ts_secs // 3600
        m = (ts_secs % 3600) // 60
        s = ts_secs % 60
        ts_fmt = f"{h:02d}:{m:02d}:{s:02d}" if h > 0 else f"{m:02d}:{s:02d}"

        if speaker != prev_speaker:
            f.write(f"\n## {speaker}\n\n")

        f.write(f"**[{ts_fmt}]** {text}\n\n")
        prev_speaker = speaker

print(f"\nOutput: {output_file}")
size = os.path.getsize(output_file)
print(f"Size: {size} bytes ({size/1024:.1f} KB)")
