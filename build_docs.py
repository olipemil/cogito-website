#!/usr/bin/env python3
"""
Build COGITO documentation with Sphinx for both HTML and Jekyll integration.
"""

import os
import subprocess
import sys
from pathlib import Path

def add_jekyll_frontmatter(md_file, title, nav_order):
    """Add Jekyll front matter to markdown files."""
    content = md_file.read_text()

    frontmatter = f"""---
layout: default
title: {title}
nav_order: {nav_order}
parent: API Documentation
---

"""

    # Add CSS for API documentation styling
    css_block = """
<link rel="stylesheet" href="{{ '/docs/_static/api-docs.css' | relative_url }}">

"""

    new_content = frontmatter + css_block + content
    md_file.write_text(new_content)

def main():
    """Build HTML and Jekyll-compatible documentation."""

    docs_dir = Path(__file__).parent / "docs"
    api_dir = Path(__file__).parent / "api"

    print("Building COGITO documentation...")

    # Change to docs directory
    os.chdir(docs_dir)

    try:
        # Build HTML documentation
        print("📋 Building HTML documentation...")
        result = subprocess.run([
            "sphinx-build", "-b", "html", ".", "_build/html"
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error building HTML docs: {result.stderr}")
            sys.exit(1)

        # Build markdown documentation for Jekyll
        print("📋 Building Jekyll markdown documentation...")
        result = subprocess.run([
            "sphinx-build", "-b", "markdown", ".", "_build/markdown"
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error building markdown docs: {result.stderr}")
            sys.exit(1)

        # Process markdown files for Jekyll
        print("📋 Processing markdown files for Jekyll...")

        # Create api directory if it doesn't exist
        api_dir.mkdir(exist_ok=True)

        md_dir = docs_dir / "_build/markdown"

        # File mapping for Jekyll
        file_mapping = {
            'index.md': {'title': 'API Documentation', 'nav_order': 1},
            'COGITO.md': {'title': 'COGITO Core API', 'nav_order': 2},
            'COGITOpost.md': {'title': 'COGITOpost API', 'nav_order': 3},
            'COGITOico.md': {'title': 'COGITOico API', 'nav_order': 4}
        }

        for md_file_name, file_info in file_mapping.items():
            src_file = md_dir / md_file_name
            dest_file = api_dir / md_file_name

            if src_file.exists():
                # Copy and process the file
                dest_file.write_text(src_file.read_text())
                add_jekyll_frontmatter(dest_file, file_info['title'], file_info['nav_order'])
                print(f"✅ Processed {md_file_name} for Jekyll")

        print("\n🎉 Documentation built successfully!")
        print(f"📁 HTML files: {docs_dir / '_build/html'}")
        print(f"📁 Jekyll files: {api_dir}")
        print(f"🌐 Open HTML: {docs_dir / '_build/html/index.html'}")

    except FileNotFoundError:
        print("Error: sphinx-build not found. Please install:")
        print("pip install sphinx sphinx-rtd-theme sphinx-markdown-builder")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()