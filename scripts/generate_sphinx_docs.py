#!/usr/bin/env python3
"""
Generate Sphinx-based API documentation for COGITO.
This replaces the old generate_api_docs.py with proper Sphinx autodoc.
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    """Generate Sphinx markdown documentation."""

    # Get the directory paths
    script_dir = Path(__file__).parent
    sphinx_docs_dir = script_dir / "sphinx-docs"
    api_sphinx_dir = script_dir / "api-sphinx"
    api_dir = script_dir.parent / "api"

    print("Generating Sphinx API documentation...")

    # Change to sphinx-docs directory
    os.chdir(sphinx_docs_dir)

    try:
        # Run sphinx-build to generate markdown
        result = subprocess.run([
            "sphinx-build", "-b", "markdown", ".", str(api_sphinx_dir)
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error generating Sphinx docs: {result.stderr}")
            sys.exit(1)

        print("Sphinx build completed successfully!")

        # Copy generated files to api directory
        if api_sphinx_dir.exists():
            for md_file in api_sphinx_dir.glob("*.md"):
                dest_file = api_dir / md_file.name
                dest_file.write_text(md_file.read_text())
                print(f"Copied {md_file.name} to API directory")

        print("✅ Sphinx API documentation generated successfully!")

    except FileNotFoundError:
        print("Error: sphinx-build not found. Please install Sphinx:")
        print("pip install sphinx sphinx-markdown-builder")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()