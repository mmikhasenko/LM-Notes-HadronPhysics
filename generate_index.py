#!/usr/bin/env python3
"""
Advanced index generator with better error handling and support for different file patterns.
This script automatically generates index.html based on actual lecture files present.
"""

import os
import re
import glob
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set

# Import configuration
try:
    from lecture_config import EXPECTED_LECTURES, SUPPORTED_PATTERNS, SKIP_FILES, STYLES
except ImportError:
    # Fallback configuration if config file is not available
    EXPECTED_LECTURES = {
        2024: range(1, 15),  # Lectures 1-14 for 2024
        2025: range(1, 15),  # Lectures 1-14 for 2025
    }
    SUPPORTED_PATTERNS = [
        r'(\d{4})-Lecture-(\d+)\.md',  # 2024-Lecture-01.md
        r'Lecture-(\d+)\.md',          # Lecture-01.md (fallback)
    ]
    SKIP_FILES = ['index.qmd', '_metadata.yml', '_quarto.yml']
    STYLES = {
        'available_color': '#17365c',
        'missing_color': '#999',
        'missing_text_color': '#ccc',
        'header_color': '#17365c',
        'accent_color': '#8dae10',
    }

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class LectureIndexGenerator:
    def __init__(self, lectures_dir: str = "Lectures"):
        self.lectures_dir = lectures_dir
        self.supported_patterns = SUPPORTED_PATTERNS
        self.expected_lectures = EXPECTED_LECTURES
        self.skip_files = SKIP_FILES
        self.styles = STYLES
    
    def extract_lecture_info(self, filename: str) -> Optional[Tuple[int, int]]:
        """Extract year and lecture number from filename using multiple patterns"""
        for pattern in self.supported_patterns:
            match = re.match(pattern, filename)
            if match:
                if len(match.groups()) == 2:
                    year = int(match.group(1))
                    lecture_num = int(match.group(2))
                    return year, lecture_num
                elif len(match.groups()) == 1:
                    # Fallback pattern without year
                    lecture_num = int(match.group(1))
                    # Try to extract year from directory or use current year
                    return 2024, lecture_num
        return None
    
    def get_lecture_files(self) -> Dict[int, List[Tuple[int, str]]]:
        """Get all lecture files organized by year"""
        lectures = {}
        
        if not os.path.exists(self.lectures_dir):
            logger.error(f"Directory {self.lectures_dir} not found")
            return {}
        
        # Find all Markdown files
        md_files = glob.glob(os.path.join(self.lectures_dir, "*.md"))
        
        if not md_files:
            logger.warning(f"No Markdown files found in {self.lectures_dir}")
            return {}
        
        for file_path in md_files:
            filename = os.path.basename(file_path)
            
            # Skip index and other non-lecture files
            if filename in self.skip_files:
                continue
                
            lecture_info = self.extract_lecture_info(filename)
            
            if lecture_info:
                year, lecture_num = lecture_info
                if year not in lectures:
                    lectures[year] = []
                lectures[year].append((lecture_num, filename.replace('.md', '.html')))
                logger.debug(f"Found lecture: {year}-Lecture-{lecture_num}")
            else:
                logger.warning(f"Could not parse filename: {filename}")
        
        # Sort lectures by number within each year
        for year in lectures:
            lectures[year].sort(key=lambda x: x[0])
        
        return lectures
    
    def get_missing_lectures(self, lectures: Dict[int, List[Tuple[int, str]]]) -> Dict[int, Set[int]]:
        """Get missing lecture numbers for each year"""
        missing = {}
        
        for year in lectures:
            existing_lectures = {lecture_num for lecture_num, _ in lectures[year]}
            expected_range = self.expected_lectures.get(year, range(1, 15))
            missing_lectures = set(expected_range) - existing_lectures
            if missing_lectures:
                missing[year] = missing_lectures
        
        return missing
    
    def generate_html_content(self, lectures: Dict[int, List[Tuple[int, str]]]) -> str:
        """Generate the HTML content"""
        
        # Sort years in descending order (newest first)
        years = sorted(lectures.keys(), reverse=True)
        
        if not years:
            logger.error("No valid lecture files found")
            return ""
        
        # Get missing lectures
        missing_lectures = self.get_missing_lectures(lectures)
        
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hadron Physics - Summer Semester 2024 - Ruhr University Bochum</title>
    <style>
        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e7e7e7; /* RUB-Grau */
        }}
        header {{
            width: 100%;
            background-color: #17365c; /* RUB-Blau */
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .header-buttons {{
            display: flex;
            gap: 20px;
        }}
        .header-buttons a {{
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: white;
            font-weight: bold;
            background-color: #8dae10; /* RUB-Grün */
            padding: 10px 20px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}
        .header-buttons a:hover {{
            background-color: #6b8c0e; /* Darker shade of RUB-Grün */
        }}
        .header-buttons img {{
            width: 20px;
            height: 20px;
            margin-right: 8px;
        }}
        h1 {{
            color: #17365c; /* RUB-Blau */
            text-align: center;
        }}
        .container {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin: 20px 0;
        }}
        .lecture-box {{
            background-color: #17365c; /* RUB-Blau */
            color: white;
            padding: 20px;
            margin: 10px;
            text-align: center;
            text-decoration: none;
            border-radius: 15px;
            width: 100px;
            transition: background-color 0.3s;
        }}
        .lecture-box:hover {{
            color: white;
            background-color: #122a49; /* Darker shade of RUB-Blau */
        }}
        .lecture-box.missing {{
            background-color: #999; /* Gray for missing lectures */
            color: #ccc;
            cursor: not-allowed;
            opacity: 0.7;
        }}
        .lecture-box.missing:hover {{
            background-color: #999; /* Keep gray on hover */
            color: #ccc;
        }}
        .stats {{
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin: 10px 0;
        }}
        .legend {{
            text-align: center;
            color: #666;
            font-size: 0.8em;
            margin: 10px 0;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-buttons">
            <a href="https://github.com/mmikhasenko/LM-Notes-HadronPhysics" target="_blank">
                <img src="github-mark.png" alt="GitHub Logo">
                Code
            </a>
            <a href="https://moodle.ruhr-uni-bochum.de/course/view.php?id=58809" target="_blank">Moodle Course</a>
        </div>
    </header>
    <h1>Hadron Physics</h1>
    <h2>Summer Semester 2024 - Ruhr University Bochum</h2>
    
    <h2>Lectures</h2>
'''
        
        # Generate sections for each year
        for year in years:
            html_content += f'''    <details open>
        <summary style="font-size: 1.2em; font-weight: bold; color: #17365c; margin: 10px 0;">{year}</summary>
        <div class="container">
'''
            
            # Get all expected lectures for this year
            expected_range = self.expected_lectures.get(year, range(1, 15))
            existing_lectures = {lecture_num for lecture_num, _ in lectures[year]}
            
            # Generate buttons for all expected lectures
            for lecture_num in expected_range:
                if lecture_num in existing_lectures:
                    # Find the HTML filename for this lecture
                    html_filename = next(html_file for num, html_file in lectures[year] if num == lecture_num)
                    html_content += f'            <a href="{html_filename}" class="lecture-box">Lecture {lecture_num}</a>\n'
                else:
                    # Missing lecture - create unclickable button
                    html_content += f'            <span class="lecture-box missing" title="Material not available">Lecture {lecture_num}</span>\n'
            
            html_content += '''        </div>
    </details>
'''
        
        # Add statistics
        total_lectures = sum(len(lectures[year]) for year in lectures)
        total_missing = sum(len(missing_lectures.get(year, set())) for year in missing_lectures)
        total_expected = sum(len(self.expected_lectures.get(year, range(1, 15))) for year in years)
        
        html_content += f'''    <div class="stats">
        Available: {total_lectures} lectures | Missing: {total_missing} lectures | Total: {total_expected} lectures
    </div>
    <div class="legend">
        <strong>Legend:</strong> Blue buttons = Available | Gray buttons = Missing material
    </div>
</body>
</html>'''
        
        return html_content
    
    def generate_index(self, output_file: Optional[str] = None) -> bool:
        """Generate the index.html file"""
        
        if output_file is None:
            output_file = os.path.join(self.lectures_dir, "index.html")
        
        try:
            lectures = self.get_lecture_files()
            
            if not lectures:
                logger.error("No lecture files found")
                return False
            
            html_content = self.generate_html_content(lectures)
            
            if not html_content:
                logger.error("Failed to generate HTML content")
                return False
            
            # Write the file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Print summary
            total_lectures = sum(len(lectures[year]) for year in lectures)
            missing_lectures = self.get_missing_lectures(lectures)
            total_missing = sum(len(missing_lectures.get(year, set())) for year in missing_lectures)
            
            logger.info(f"Generated index.html with {total_lectures} available lectures")
            if total_missing > 0:
                logger.info(f"Missing {total_missing} lectures (shown as gray buttons)")
            
            for year in sorted(lectures.keys(), reverse=True):
                missing_count = len(missing_lectures.get(year, set()))
                logger.info(f"  {year}: {len(lectures[year])} available, {missing_count} missing")
            
            logger.info(f"Index file generated: {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error generating index: {e}")
            return False

def main():
    """Main function with enhanced statistics and error handling"""
    print("🔄 Generating index.html...")
    
    # Check if we're in the right directory
    if not os.path.exists("Lectures"):
        print("❌ Error: Lectures directory not found. Please run this script from the project root.")
        exit(1)
    
    generator = LectureIndexGenerator()
    success = generator.generate_index()
    
    if success:
        print("✅ Index generation completed successfully!")
        
        # Show summary statistics
        lectures = generator.get_lecture_files()
        missing_lectures = generator.get_missing_lectures(lectures)
        
        total_available = sum(len(lectures[year]) for year in lectures)
        total_missing = sum(len(missing_lectures.get(year, set())) for year in missing_lectures)
        
        print("📊 Summary:")
        for year in sorted(lectures.keys(), reverse=True):
            missing_count = len(missing_lectures.get(year, set()))
            print(f"   - {year}: {len(lectures[year])} available, {missing_count} missing")
        
        print(f"📝 Missing lectures are shown as gray, unclickable buttons")
        print(f"📄 Index file: Lectures/index.html")
    else:
        print("❌ Index generation failed!")
        exit(1)

if __name__ == "__main__":
    main() 