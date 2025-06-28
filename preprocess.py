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
    content = re.sub(
        # Pattern breakdown:
        r'(\n(?:> )?[^-].*\n)'          # Group 1: A line that doesn't start with a dash:
                                        #   \n               → starts with a newline
                                        #   (?:> )?          → optionally starts with "> "
                                        #   [^-].*           → line must not start with "-" (avoids matching list items)
                                        #   \n               → ends with newline (captures a full line)
        r'((> )?(?:1\.|-|\*)\s)',       # Group 2: A list item line starting with:
                                        #   (Group 3: optional "> ")  
                                        #   followed by "1.", "-" or "*"  
                                        #   then a space (to avoid matching things like "1.something")
    
        # Replacement logic:
        lambda m: (
            f"{m.group(1)}"             # Reinsert the first line (non-list content before the list)
            f"{'>' if m.group(3) else ''}\n"  # If the bullet line had a "> ", add a new "> \n" to split it
            f"{m.group(2)}"             # Reinsert the bullet line
        ),
    
        content,
        re.MULTILINE # `.` is any character except newline
    )
    
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
    

    # Handle \slashed command as before
    content = re.sub(
        r'\\slashed\s*(?:\{([^\}]+)\}|([a-zA-Z]))',
        lambda m: (
            f"\\mathrlap{{\,/}}{m.group(1) or m.group(2)}"
            if (m.group(1) or m.group(2)).isupper()
            else f"\\mathrlap{{/}}{m.group(1) or m.group(2)}"
        ),
        content
    )



    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    directory = sys.argv[1]
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            transform_file(os.path.join(directory, filename))
