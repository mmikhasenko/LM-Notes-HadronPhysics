#!/usr/bin/env python3
"""
Post-process HTML files to fix section numbering.
Replaces 0.1, 0.2, etc. with correct sequential numbers across all files.
"""

import os
import re
import glob
from pathlib import Path

def extract_lecture_info(filename):
    """Extract year and lecture number from filename"""
    pattern = r'(\d{4})-Lecture-(\d+)\.html'
    match = re.match(pattern, filename)
    if match:
        year = int(match.group(1))
        lecture_num = int(match.group(2))
        return year, lecture_num
    return None, None

def get_lecture_order(html_dir):
    """Get ordered list of HTML files with their target section numbers"""
    lectures = []
    
    # Find all HTML files
    html_files = glob.glob(os.path.join(html_dir, "*.html"))
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        year, lecture_num = extract_lecture_info(filename)
        
        if year and lecture_num:
            lectures.append((year, lecture_num, file_path))
    
    # Sort by year and lecture number
    lectures.sort(key=lambda x: (x[0], x[1]))
    
    # Assign section numbers (starting from 1)
    for i, (year, lecture_num, file_path) in enumerate(lectures, 1):
        lectures[i-1] = (year, lecture_num, file_path, i)
    
    return lectures

def fix_section_numbers_in_html(file_path, target_section_number):
    """Fix section numbers in HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all section numbers in the file (0.1, 0.2, etc.)
    # and replace them with the target section number
    def replace_section_number(match):
        section_num = int(match.group(1))
        return f"{target_section_number}.{section_num}"
    
    # Replace all occurrences of "0.X" with "target_section_number.X"
    content = re.sub(r'0\.(\d+)', replace_section_number, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_dir = "Lectures"  # Directory containing HTML files
    
    lectures = get_lecture_order(html_dir)
    
    print("Fixing section numbers in HTML files:")
    for year, lecture_num, file_path, section_num in lectures:
        filename = os.path.basename(file_path)
        print(f"  {filename} -> section {section_num}")
        fix_section_numbers_in_html(file_path, section_num)
    
    print(f"\nProcessed {len(lectures)} HTML files")

if __name__ == "__main__":
    main() 