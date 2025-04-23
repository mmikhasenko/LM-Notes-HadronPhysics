import sys
import re
import os

def transform_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(
        r'^> \[!(\w+)\]\s*\n((?:^> ?(.*\n)?|)(.*))',
        lambda m: f"::: callout-{m.group(1).lower()}\n" + (m.group(3).strip() if m.group(3) else m.group(4).strip()) + "\n:::",
        content,
        flags=re.MULTILINE
    )

    # Convert ```math blocks to $$...$$
    content = re.sub(
        r'```math\s*\n(.*?)\n```',
        lambda m: f"$$\n{m.group(1)}\n$$",
        content,
        flags=re.DOTALL
    )

    # Convert $`math`$ to $math$
    content = re.sub(
        r'\$\`(.*?)\`\$',
        lambda m: f"${m.group(1)}$",
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'\\slashed\s*(?:\{([^\}]+)\}|([a-zA-Z]))',
        lambda m: f"\\mathrlap{{/}}{m.group(1) or m.group(2)}",
        content
    )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == '__main__':
    directory = sys.argv[1]
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            transform_file(os.path.join(directory, filename))
