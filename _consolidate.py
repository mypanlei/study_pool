#!/usr/bin/env python3
"""
Consolidate all 录制文件 from Clippings/ into one deduplicated raw transcript.
"""

import re
import os
import glob

# Paths
clippings_dir = r"C:\Users\mypan\OneDrive\workspace\study_pool\Clippings"
output_dir = r"C:\Users\mypan\OneDrive\workspace\study_pool\技术经理人中级培训"
output_file = os.path.join(output_dir, "浙江省技术经纪人中级培训-科技成果转化与商业逻辑_raw.md")

# Get all 录制文件
files = sorted(glob.glob(os.path.join(clippings_dir, "录制文件*.md")),
               key=lambda x: int(re.search(r'录制文件(?:\s*(\d+))?\.md', os.path.basename(x)).group(1) or '0'))

# Step 1: Extract all speaker entries from all files
def extract_dialogues(filepath):
    """Extract (speaker, timestamp_seconds, timestamp_str, dialogue_text) tuples from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []

    # Skip frontmatter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check if line is a speaker name (Chinese chars, no colon/timestamp pattern)
        # Speaker names are like "刘锐", "高延庆", "孙老师-北航杭研院"
        speaker_match = re.match(r'^([一-鿿]+(?:[-一-鿿\w]*[一-鿿]+)?)$', line)

        if speaker_match and i + 1 < len(lines):
            speaker = speaker_match.group(1)
            # Skip if this looks like chapter title rather than speaker
            # Chapter titles have Chinese only and are longer
            if len(speaker) > 15:
                i += 1
                continue

            # Check next line for timestamp
            next_line = lines[i + 1].strip()
            # Timestamp patterns: MM:SS or H:MM:SS (e.g., "00:00", "1:02:46", "01:02:46")
            ts_match = re.match(r'^(\d{1,2}:\d{2}(?::\d{2})?)$', next_line)

            if ts_match:
                ts_str = ts_match.group(1)
                # Convert timestamp to seconds for sorting
                parts = ts_str.split(':')
                if len(parts) == 3:
                    ts_secs = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
                else:
                    ts_secs = int(parts[0]) * 60 + int(parts[1])

                # Collect dialogue text (multiple lines until next speaker or "定位到" or empty line)
                dialogue_lines = []
                j = i + 2
                while j < len(lines):
                    l = lines[j].strip()
                    if l == '' or l == '定位到正在播放位置':
                        break
                    # Check if this line starts a new speaker entry
                    if re.match(r'^[一-鿿]+(?:[-一-鿿\w]*[一-鿿]+)?$', l) and j + 1 < len(lines) and re.match(r'^\d{1,2}:\d{2}(?::\d{2})?$', lines[j+1].strip()):
                        break
                    # Skip chapter marker images
                    if l.startswith('!['):
                        j += 1
                        continue
                    dialogue_lines.append(l)
                    j += 1

                dialogue_text = ' '.join(dialogue_lines).strip()
                if dialogue_text:
                    entries.append((speaker, ts_secs, ts_str, dialogue_text))

                i = j
                continue

        i += 1

    return entries


# Extract all entries
all_entries = []
for f in files:
    basename = os.path.basename(f)
    entries = extract_dialogues(f)
    print(f"{basename}: {len(entries)} entries extracted")
    all_entries.extend(entries)

print(f"\nTotal entries before dedup: {len(all_entries)}")

# Step 2: Deduplicate - same speaker + same timestamp + similar text
# Sort by timestamp first
all_entries.sort(key=lambda x: (x[1], x[0]))

# Dedup: keep first occurrence of each (speaker, timestamp_seconds) pair
seen = set()
deduped = []
for speaker, ts_secs, ts_str, text in all_entries:
    key = (speaker, ts_secs)
    if key not in seen:
        seen.add(key)
        deduped.append((speaker, ts_secs, ts_str, text))

print(f"Total entries after dedup: {len(deduped)}")

# Step 3: Write consolidated output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("---\n")
    f.write("title: 浙江省技术经纪人中级培训 - 会议文字记录（整合去重）\n")
    f.write("created: 2026-06-17\n")
    f.write("source: https://meeting.tencent.com/cw/KwWaeJW476\n")
    f.write("tags:\n")
    f.write("  - 技术经理人\n")
    f.write("  - 中级培训\n")
    f.write("  - 会议记录\n")
    f.write("  - raw\n")
    f.write("---\n\n")
    f.write("# 浙江省技术经纪人中级培训 - 会议文字记录\n\n")
    f.write("> 来源：腾讯会议录制\n")
    f.write("> 日期：2026-06-17\n")
    f.write("> 时长：2:33:13\n")
    f.write("> 整合：从 Clippings 录制文件中提取去重合并\n\n")
    f.write("---\n\n")

    prev_speaker = None
    for speaker, ts_secs, ts_str, text in deduped:
        # Format timestamp nicely
        hours = ts_secs // 3600
        mins = (ts_secs % 3600) // 60
        secs = ts_secs % 60
        if hours > 0:
            formatted_ts = f"{hours:02d}:{mins:02d}:{secs:02d}"
        else:
            formatted_ts = f"{mins:02d}:{secs:02d}"

        if speaker != prev_speaker:
            f.write(f"\n### {speaker}\n\n")
            prev_speaker = speaker

        f.write(f"**[{formatted_ts}]** {text}\n\n")

print(f"\nOutput written to: {output_file}")
print(f"File size: {os.path.getsize(output_file)} bytes")
