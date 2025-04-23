#!/bin/bash
# This script converts a Markdown file to HTML using cmark-gfm.
# run with
# 
# ./convert.sh Lectures/Lecture-01.md Lecture-01.html


# Check if input and output arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <input_markdown_file> <output_html_file>"
    exit 1
fi

input_file=$1
output_file=$2

echo "Converting $input_file to $output_file..."

# Convert Markdown to HTML using cmark-gfm directly without admonition processing
cmark-gfm --unsafe --extension table --extension tasklist --extension autolink "$input_file" > temp_content.html

# Create HTML file with template - write head section
cat > "$output_file" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
EOF

# Add title dynamically
echo "    <title>$(basename "$input_file" .md)</title>" >> "$output_file"

# Continue with the rest of the head section
cat >> "$output_file" << 'EOF'
    <link rel="stylesheet" href="https://unpkg.com/@primer/css@latest/build.css">
    <!-- MathJax for LaTeX rendering -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true,
                processEnvironments: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }
        };
    </script>
</head>
<body class="markdown-body container-lg px-3 my-5">
EOF

# Add the content to the HTML file
cat temp_content.html >> "$output_file"

# Close the HTML file
echo "</body></html>" >> "$output_file"

# Clean up temporary file
rm temp_content.html

echo "Conversion complete!"
