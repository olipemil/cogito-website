#!/usr/bin/env python3
"""
Preprocessing script to temporarily convert @param format to Google-style docstrings
for proper Sphinx formatting, then restore after building.
"""

import os
import re
import shutil
from pathlib import Path

COGITO_PATH = Path("../../../COGITO")
BACKUP_PATH = Path("./cogito_backup")

def backup_original_files():
    """Create backup of original Python files."""
    if BACKUP_PATH.exists():
        shutil.rmtree(BACKUP_PATH)
    shutil.copytree(COGITO_PATH, BACKUP_PATH)
    print(f"✓ Backed up original files to {BACKUP_PATH}")

def restore_original_files():
    """Restore original Python files from backup."""
    if BACKUP_PATH.exists():
        # Remove current COGITO directory
        if COGITO_PATH.exists():
            shutil.rmtree(COGITO_PATH)
        # Restore from backup
        shutil.copytree(BACKUP_PATH, COGITO_PATH)
        # Clean up backup
        shutil.rmtree(BACKUP_PATH)
        print(f"✓ Restored original files from backup")

def convert_param_format_to_google(docstring):
    """Convert @param format to Google-style docstring format."""
    if not docstring:
        return docstring

    lines = docstring.split('\n')
    converted_lines = []
    args_section = []
    returns_section = []
    raises_section = []
    in_args = False
    in_returns = False
    in_raises = False

    for line in lines:
        stripped = line.strip()

        # Handle @param lines
        if stripped.startswith('@param '):
            if not in_args:
                in_args = True
                in_returns = False
                in_raises = False
            # Extract parameter info: @param name: description
            match = re.match(r'@param\s+(\w+):\s*(.*)', stripped)
            if match:
                param_name, description = match.groups()
                args_section.append(f"        {param_name}: {description}")

        # Handle @return lines
        elif stripped.startswith('@return'):
            if not in_returns:
                in_returns = True
                in_args = False
                in_raises = False
            # Extract return info: @return: description or @returns: description
            match = re.match(r'@returns?:?\s*(.*)', stripped)
            if match:
                description = match.group(1)
                if description:
                    returns_section.append(f"        {description}")

        # Handle @raises lines
        elif stripped.startswith('@raises '):
            if not in_raises:
                in_raises = True
                in_args = False
                in_returns = False
            # Extract raises info: @raises Exception: description
            match = re.match(r'@raises\s+(\w+):\s*(.*)', stripped)
            if match:
                exception, description = match.groups()
                raises_section.append(f"        {exception}: {description}")

        # Regular docstring lines
        else:
            # If we were collecting special sections, add them now
            if (in_args or in_returns or in_raises) and stripped and not stripped.startswith('@'):
                in_args = in_returns = in_raises = False

            # Only add non-@param/@return/@raises lines
            if not any(stripped.startswith(prefix) for prefix in ['@param ', '@return', '@raises ']):
                converted_lines.append(line)

    # Add collected sections to the docstring
    result_lines = converted_lines

    if args_section:
        result_lines.append("")
        result_lines.append("    Args:")
        result_lines.extend(args_section)

    if returns_section:
        result_lines.append("")
        result_lines.append("    Returns:")
        result_lines.extend(returns_section)

    if raises_section:
        result_lines.append("")
        result_lines.append("    Raises:")
        result_lines.extend(raises_section)

    return '\n'.join(result_lines)

def process_python_file(file_path):
    """Process a single Python file to convert @param format."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all docstrings and convert them
    # This regex finds triple-quoted strings that are likely docstrings
    pattern = r'(""")(.*?)("""|\'\'\'.*?\'\'\')'

    def replace_docstring(match):
        start_quote = match.group(1)
        docstring_content = match.group(2)
        end_quote = match.group(3)

        converted_content = convert_param_format_to_google(docstring_content)
        return start_quote + converted_content + '"""'

    # Apply conversion
    converted_content = re.sub(pattern, replace_docstring, content, flags=re.DOTALL)

    # Write back the converted content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

def convert_all_files():
    """Convert all Python files in COGITO directory."""
    python_files = list(COGITO_PATH.glob("*.py"))

    for py_file in python_files:
        print(f"Converting {py_file.name}...")
        process_python_file(py_file)

    print(f"✓ Converted {len(python_files)} Python files")

def main():
    """Main function to handle the preprocessing."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python preprocess_docstrings.py [convert|restore]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "convert":
        backup_original_files()
        convert_all_files()
        print("✓ Files converted for Sphinx processing")

    elif action == "restore":
        restore_original_files()
        print("✓ Original files restored")

    else:
        print("Error: Action must be 'convert' or 'restore'")
        sys.exit(1)

if __name__ == "__main__":
    main()