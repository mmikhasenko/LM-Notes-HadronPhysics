#!/usr/bin/env python3
"""
Configuration file for lecture index generation.
Adjust the expected lecture ranges for different years here.
"""

# Expected lecture ranges for each year
# Format: year: range(start, end) where end is exclusive
EXPECTED_LECTURES = {
    2024: range(1, 14),  # Lectures 1-14 for 2024
    2025: range(1, 14),  # Lectures 1-14 for 2025
    # Add more years as needed:
    # 2026: range(1, 13),  # Lectures 1-12 for 2026
}

# File patterns to recognize lecture files
SUPPORTED_PATTERNS = [
    r'(\d{4})-Lecture-(\d+)\.md',  # 2024-Lecture-01.md
    r'Lecture-(\d+)\.md',          # Lecture-01.md (fallback)
]

# Files to skip during processing
SKIP_FILES = [
    'index.qmd',
    '_metadata.yml',
    '_quarto.yml',
]

# Styling configuration
STYLES = {
    'available_color': '#17365c',      # RUB-Blau for available lectures
    'missing_color': '#999',           # Gray for missing lectures
    'missing_text_color': '#ccc',      # Light gray text for missing lectures
    'header_color': '#17365c',         # RUB-Blau for headers
    'accent_color': '#8dae10',         # RUB-Grün for accent elements
} 