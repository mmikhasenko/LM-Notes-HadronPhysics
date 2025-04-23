import sys
import re
import os

def transform_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Convert [!NOTE] style callouts
    content = re.sub(
        r'^> \[!(\w+)\]\s*\n((?:^> .*\n?)*)',
        lambda m: f"::: .callout-{m.group(1).lower()}\n" + re.sub(r'^> ?', '', m.group(2), flags=re.MULTILINE) + "\n:::",
        content,
        flags=re.MULTILINE
    )

    # Convert ```math blocks
    content = re.sub(
        r'```math\s*\n(.*?)\n```',
        lambda m: f"$$\n{m.group(1)}\n$$",
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == '__main__':
    directory = sys.argv[1]
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            transform_file(os.path.join(directory, filename))
