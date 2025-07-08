import sys
import re
import os
import logging
logger = logging.getLogger("callout_replacer")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # set to INFO or WARNING to reduce output

def transform_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read().replace("```latex", "```math")

    
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
