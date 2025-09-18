#!/usr/bin/env python3
"""
Extract ReadTheDocs content and convert to Jekyll format.
"""

import re
from pathlib import Path

def extract_content_from_html(html_file):
    """Extract the main documentation content from ReadTheDocs HTML using regex."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the main content section between the articleBody div tags
    pattern = r'<div itemprop="articleBody">\s*(.*?)\s*</div>'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1).strip()

    # Fallback: look for section with module content
    pattern = r'(<section id="module-[^"]*">.*?</section>)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1).strip()

    return None

def create_jekyll_page(module_name, title, content):
    """Create a Jekyll page with ReadTheDocs layout."""

    frontmatter = f"""---
layout: readthedocs
title: {title}
module: {module_name}
nav_order: {2 if module_name == 'cogito' else 3 if module_name == 'cogitopost' else 4}
parent: API Documentation
---

"""

    # Clean up the content to work with Jekyll
    # Fix relative links to assets
    content = content.replace('href="_static/', f'href="{{{{ \'/assets/\' | relative_url }}}}"')
    content = content.replace('src="_static/', f'src="{{{{ \'/assets/\' | relative_url }}}}"')

    # Remove the outer div wrapper if present
    if content.startswith('<div itemprop="articleBody">'):
        content = content[len('<div itemprop="articleBody">'):-6]  # Remove opening and closing div

    return frontmatter + content

def main():
    """Main function to convert ReadTheDocs files to Jekyll."""

    docs_dir = Path('docs/_build/html')
    api_dir = Path('api')

    # File mappings
    files_to_convert = {
        'COGITO.html': {'module': 'cogito', 'title': 'COGITO Core API'},
        'COGITOpost.html': {'module': 'cogitopost', 'title': 'COGITOpost API'},
        'COGITOico.html': {'module': 'cogitoico', 'title': 'COGITOico API'}
    }

    for html_file, config in files_to_convert.items():
        html_path = docs_dir / html_file

        if html_path.exists():
            print(f"Processing {html_file}...")

            # Extract content
            content = extract_content_from_html(html_path)

            if content:
                # Create Jekyll page
                jekyll_content = create_jekyll_page(
                    config['module'],
                    config['title'],
                    content
                )

                # Write to Jekyll API directory
                output_file = api_dir / f"{config['module']}.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(jekyll_content)

                print(f"✅ Created {output_file}")
            else:
                print(f"❌ Could not extract content from {html_file}")
        else:
            print(f"❌ File not found: {html_path}")

if __name__ == "__main__":
    main()