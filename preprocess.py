import sys
import re
import os

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
    pattern = re.compile(
        r'^> \[!(\w+)\]\s*\n'          # Header line: > [!TAG]
        r'((?:^>.*\n?)*)',             # All following lines starting with >
        flags=re.MULTILINE
    )

    def callout_replacer(m):
        tag = m.group(1).lower()
        block = m.group(2)

        # Remove leading '> ' or '>' from each line in the block
        lines = [line[2:] if line.startswith('> ') else line[1:] for line in block.splitlines()]
        content = "\n".join(lines).strip()

        # Now convert ```math blocks inside content to $$...$$
        content = re.sub(
            r'```math\s*\n(.*?)\n```',
            lambda mm: f"$$\n{mm.group(1)}\n$$",
            content,
            flags=re.DOTALL
        )

        return f"::: callout-{tag}\n{content}\n:::"

    content = pattern.sub(callout_replacer, content)

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
