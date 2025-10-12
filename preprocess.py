import sys
import yaml
import re
import os
import logging
from pathlib import Path
from typing import Callable
from collections import defaultdict
logger = logging.getLogger("callout_replacer")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # set to INFO or WARNING to reduce output

import json
import re

def get_metadata(basename, authors):
    print(basename)
    match = re.fullmatch(r"([0-9]{4})-Lecture-([0-9]{1,2}).md", basename)
    year = int(match.group(1))
    lecture = int(match.group(2))
    lecture_key = f"Lecture {lecture}"
    year_key = str(year)
    metadata = authors.get(year_key, {}).get(lecture_key, {})
    presenter = metadata.get("presenter", "Unknown")
    note_taker = metadata.get("note_taker", "Unknown")
    return (f"({year}) Lecture {lecture}", presenter, note_taker, str(year), "html")



def build_preamble(title: str, presenter: str, note_taker: str,
                   date: str, fmt: str) -> str:
    """
    Return a YAML front‑matter block that Quarto will recognise.
    """
    preamble_dict = {
        "title": title,
        "author": "",          # optional static author
        "presenter": presenter,
        "note_taker": note_taker,
        "date": date,
        "format": fmt
    }
    # Convert dict → YAML string
    yaml_block = yaml.safe_dump(preamble_dict, sort_keys=False).strip()
    return f"""---
{yaml_block}
---
"""+"""
**Presenter**: {{< meta presenter >}}

**Note Taker**: {{< meta note_taker >}}

"""

def transform_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read().replace("```latex", "```math")
    path = Path(filepath)
    try:
        with open('authors.json') as f:
            authors = json.load(f)
        title, presenter, note_taker, date, fmt = get_metadata(path.name, authors)
        preamble = build_preamble(title, presenter, note_taker, date, fmt)
        content = preamble + content
    except AttributeError:
        pass


    
    # Convert \(...\) blocks to $...$
    content = re.sub(
        r'\\\((.*?)\\\)',
        lambda m: f"${m.group(1).strip()}$",
        content,
        flags=re.DOTALL
    )
    
    # Render lists
    content = content.replace('\r\n', '\n')  # Normalize Windows line endings
    
    # Match entire callout block (header + all following lines starting with >)


    def fix_callouts(content):
        content = content.replace('\r\n', '\n')

        # Regex to match callout header line
        header_pattern = re.compile(r'^> \[!(\w+)\]\s*$', flags=re.MULTILINE)

        # Find all callout headers and process their blocks manually
        parts = []
        pos = 0
        for m in header_pattern.finditer(content):
            start = m.start()
            tag = m.group(1).lower()

            # Append text before this callout as-is
            parts.append(content[pos:start])

            # Now extract the block lines following this header
            # Start at end of header line
            block_start = content.find('\n', start) + 1
            if block_start == 0:
                # no following lines after header
                pos = start
                continue

            # Collect lines until we find next callout header or blank line or EOF
            lines = []
            idx = block_start
            content_lines = content[block_start:].split('\n')
            for i, line in enumerate(content_lines):
                # Stop if line is blank
                if line.strip() == '':
                    break
                # Stop if line is another callout header
                if re.match(r'^> \[!\w+\]', line):
                    break
                # Also accept lines that start with '>' or lines that don't but are indented continuation lines
                # So we accept lines that either start with '>' or lines that don't start with '>' but are continuation
                # We'll accept all lines until the stopping condition
                lines.append(line)

            # Remove exactly one leading '>' and optional space from each line if present
            cleaned_lines = []
            for line in lines:
                if line.startswith('> '):
                    cleaned_lines.append(line[2:])
                elif line.startswith('>'):
                    cleaned_lines.append(line[1:])
                else:
                    cleaned_lines.append(line)

            inner_content = '\n'.join(cleaned_lines).rstrip()

            parts.append(f"::: callout-{tag}\n{inner_content}\n:::")
            # Move position pointer forward
            pos = block_start + sum(len(l)+1 for l in lines)  # +1 for newline per line

        # Append the rest of the content
        parts.append(content[pos:])

        return ''.join(parts)


    def replace_all_except_first(pattern: str, repl_func: Callable[[re.Match], str], text: str) -> str:
        """
        Replace all matches of `pattern` in `text` except the first occurrence per key.
        The key is taken from capture group 1 of the pattern (adjust if your key group is different).
        `repl_func` is called with the Match for matches that should be replaced.
        """
        regex = re.compile(pattern)
        seen = set()

        def _sub(m: re.Match) -> str:
            key_group = 1
            key = m.group(key_group)
            if key in seen:
                return repl_func(m)
            else:
                seen.add(key)
                return m.group(0)  # keep the first occurrence as-is

        return regex.sub(_sub, text)




    content = fix_callouts(content)
    # Convert \[...\] blocks to $$...$$
    content = re.sub(
        r'\\\[\s*\n(.*?)\n\\\]',
        lambda m: f"$$\n{m.group(1)}\n$$",
        content,
        flags=re.DOTALL
    )
    # Convert ```math blocks to $$...$$
    content = re.sub(
        r'```math\s*\n(.*?)\n```',
        lambda m: f"$$\n{m.group(1)}\n$$",
        content,
        flags=re.DOTALL
    )
    # Convert $`...`$ to $...$
    content = re.sub(
        r'\$\`(.*?)\`\$',
        lambda m: f"${m.group(1)}$",
        content,
        flags=re.DOTALL
    )

    content = replace_all_except_first(
        r'\!\[.*\]\(images/fig([0-9]).png\)',
        lambda m: f"Refer to @fig-fg{m.group(1)}",
        content
    )

    content = re.sub(
        r'(\!\[.*\]\(images/fig([0-9]).png\))',
        lambda m: f"\n\n{m.group(1)}{{#fig-fg{m.group(2)}}}\n\n",
        content,
    )


    content = re.sub(
        r'\bRefer to Figure ([0-9]+)\b',
        lambda m: f"Refer to @fig-fg{m.group(1)}",
        content,
        flags=re.IGNORECASE,
    )

    # Render lists - add space before first list item, but not between items
    # Use a two-step approach: first mark list items, then add spacing
    lines = content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        # Check if this line is a list item
        is_list_item = bool(re.match(r'^(\d+\.|[-*])\s+', line))
        
        if is_list_item:
            # Check if previous line was also a list item
            prev_is_list_item = (i > 0 and bool(re.match(r'^(\d+\.|[-*])\s+', lines[i-1])))
            
            # Add blank line before if this is the first list item in a sequence
            if not prev_is_list_item and i > 0 and lines[i-1].strip() != '':
                new_lines.append('')
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)

    # Handle \slashed command as before
    content = re.sub(
        r'\\slashed\s*(?:\{([^\}]+)\}|([a-zA-Z]))',
        lambda m: (
            rf"\mathrlap{{\,/}}{m.group(1) or m.group(2)}"
            if (m.group(1) or m.group(2)).isupper()
            else rf"\mathrlap{{/}}{m.group(1) or m.group(2)}"
        ),
        content
    )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    directory = sys.argv[1]
    
    print("Applying content transformations:")
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            print(f"  Processing {filename}")
            transform_file(filepath)
    
    print(f"\nProcessed all markdown files with content transformations")
