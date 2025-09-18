#!/usr/bin/env python3
"""
SAFE preprocessing script that creates temporary copies of COGITO files within
cogito-website directory, processes them for Sphinx, then cleans up.
NEVER touches the original COGITO repository.
"""

import os
import re
import shutil
from pathlib import Path

# All paths are relative to cogito-website directory - NEVER go outside!
ORIGINAL_COGITO_PATH = Path("../../../COGITO")  # READ ONLY - never modified
TEMP_COGITO_PATH = Path("./temp_cogito_copy")   # Temporary copy within cogito-website
SPHINX_DOCS_PATH = Path(".")

def create_temp_copy():
    """Create a temporary copy of COGITO files within cogito-website directory."""
    # Remove any existing temp copy
    if TEMP_COGITO_PATH.exists():
        shutil.rmtree(TEMP_COGITO_PATH)

    # Create fresh copy within cogito-website
    print(f"Creating temporary copy at {TEMP_COGITO_PATH.absolute()}")
    shutil.copytree(ORIGINAL_COGITO_PATH, TEMP_COGITO_PATH)
    print(f"✓ Created safe temporary copy in cogito-website directory")

def cleanup_temp_copy():
    """Remove the temporary copy."""
    if TEMP_COGITO_PATH.exists():
        shutil.rmtree(TEMP_COGITO_PATH)
        print(f"✓ Cleaned up temporary copy")

def convert_param_format_to_sphinx(docstring):
    """Convert @param format to proper Sphinx format and fix structure."""
    if not docstring:
        return docstring

    lines = docstring.split('\n')
    converted_lines = []

    for i, line in enumerate(lines):
        # Convert @param to :param format
        if line.strip().startswith('@param '):
            line = line.replace('@param ', ':param ')
        elif line.strip().startswith('@return'):
            line = line.replace('@return', ':returns')
        elif line.strip().startswith('@raises '):
            line = line.replace('@raises ', ':raises ')

        converted_lines.append(line)

    # Now fix structural issues for proper Sphinx parsing
    fixed_lines = []
    i = 0
    while i < len(converted_lines):
        line = converted_lines[i]
        stripped = line.strip()

        # If this is a :param line, ensure proper formatting
        if stripped.startswith(':param '):
            # Add blank line before first param if needed
            if fixed_lines and fixed_lines[-1].strip() and not fixed_lines[-1].strip().startswith(':'):
                fixed_lines.append('')

            fixed_lines.append(line)

            # Look ahead to group all parameters together
            j = i + 1
            while j < len(converted_lines) and converted_lines[j].strip().startswith(':param '):
                fixed_lines.append(converted_lines[j])
                j += 1

            # Add blank line after params if there's more content
            if j < len(converted_lines) and converted_lines[j].strip():
                fixed_lines.append('')

            i = j - 1  # Will be incremented at end of loop

        # If this is a :returns line, ensure proper formatting
        elif stripped.startswith(':returns'):
            # Add blank line before if needed
            if fixed_lines and fixed_lines[-1].strip() and not fixed_lines[-1].strip().startswith(':'):
                fixed_lines.append('')
            fixed_lines.append(line)
            # Add blank line after if there's more content
            if i + 1 < len(converted_lines) and converted_lines[i + 1].strip():
                fixed_lines.append('')

        else:
            fixed_lines.append(line)

        i += 1

    return '\n'.join(fixed_lines)

def process_python_file(file_path):
    """Process a single Python file to convert @param format."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all docstrings and convert them - handle both """ and ''' formats
    # First handle triple double quotes
    def replace_double_docstring(match):
        start_quote = match.group(1)
        docstring_content = match.group(2)
        end_quote = match.group(3)
        converted_content = convert_param_format_to_sphinx(docstring_content)
        return start_quote + converted_content + end_quote

    # First pass: handle """ docstrings
    pattern_double = r'(""")(.*?)(""")'
    content = re.sub(pattern_double, replace_double_docstring, content, flags=re.DOTALL)

    # Second pass: handle ''' docstrings
    def replace_single_docstring(match):
        start_quote = match.group(1)
        docstring_content = match.group(2)
        end_quote = match.group(3)
        converted_content = convert_param_format_to_sphinx(docstring_content)
        return start_quote + converted_content + end_quote

    pattern_single = r'(\'\'\')(.*?)(\'\'\')'
    content = re.sub(pattern_single, replace_single_docstring, content, flags=re.DOTALL)

    # Write back the converted content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_temp_files():
    """Convert the temporary Python files."""
    python_files = list(TEMP_COGITO_PATH.glob("*.py"))

    for py_file in python_files:
        print(f"Converting {py_file.name}...")
        process_python_file(py_file)

    print(f"✓ Converted {len(python_files)} temporary files")

def update_sphinx_path():
    """Update sys.path in conf.py to point to temporary copy."""
    conf_file = SPHINX_DOCS_PATH / "conf.py"

    with open(conf_file, 'r') as f:
        content = f.read()

    # Replace the path to point to our temporary copy
    old_path = "sys.path.insert(0, os.path.abspath('../../../COGITO'))"
    new_path = "sys.path.insert(0, os.path.abspath('./temp_cogito_copy'))"

    updated_content = content.replace(old_path, new_path)

    with open(conf_file, 'w') as f:
        f.write(updated_content)

    print("✓ Updated Sphinx configuration to use temporary copy")

def restore_sphinx_path():
    """Restore original sys.path in conf.py."""
    conf_file = SPHINX_DOCS_PATH / "conf.py"

    with open(conf_file, 'r') as f:
        content = f.read()

    # Restore the original path
    old_path = "sys.path.insert(0, os.path.abspath('./temp_cogito_copy'))"
    new_path = "sys.path.insert(0, os.path.abspath('../../../COGITO'))"

    updated_content = content.replace(old_path, new_path)

    with open(conf_file, 'w') as f:
        f.write(updated_content)

    print("✓ Restored original Sphinx configuration")

def main():
    """Main function - completely safe, never touches original COGITO files."""
    import sys

    print("SAFE PREPROCESSING - Only works within cogito-website directory")
    print("Original COGITO files will NEVER be modified")
    print("=" * 60)

    if len(sys.argv) != 2:
        print("Usage: python safe_preprocess_docstrings.py [convert|cleanup]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "convert":
        try:
            create_temp_copy()
            convert_temp_files()
            update_sphinx_path()
            print("\n✅ SAFE CONVERSION COMPLETE")
            print("- Temporary copies created and processed")
            print("- Original COGITO files untouched")
            print("- Ready for Sphinx HTML generation")
            print("- Run 'sphinx-build -b html . ../../api-html/' to generate docs")
            print("- Run 'python safe_preprocess_docstrings.py cleanup' when done")

        except Exception as e:
            print(f"❌ Error during conversion: {e}")
            cleanup_temp_copy()
            restore_sphinx_path()
            sys.exit(1)

    elif action == "cleanup":
        restore_sphinx_path()
        cleanup_temp_copy()
        print("✅ CLEANUP COMPLETE - All temporary files removed")

    else:
        print("Error: Action must be 'convert' or 'cleanup'")
        sys.exit(1)

if __name__ == "__main__":
    main()