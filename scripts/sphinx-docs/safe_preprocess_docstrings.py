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