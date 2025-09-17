#!/usr/bin/env python3
"""
Generate API documentation from COGITO source code and convert to Jekyll markdown.
"""

import os
import sys
import re
import ast
import inspect
from pathlib import Path

# Add COGITO to path
sys.path.insert(0, '../../COGITO')

def extract_docstring_and_methods(file_path):
    """Extract class docstrings and method information from Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content)

        classes = []
        functions = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_info = {
                    'name': node.name,
                    'docstring': ast.get_docstring(node) or '',
                    'methods': [],
                    'line_number': node.lineno
                }

                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_info = {
                            'name': item.name,
                            'docstring': ast.get_docstring(item) or '',
                            'args': [arg.arg for arg in item.args.args],
                            'line_number': item.lineno
                        }
                        class_info['methods'].append(method_info)

                classes.append(class_info)

            elif isinstance(node, ast.FunctionDef) and node.col_offset == 0:
                # Top-level functions
                function_info = {
                    'name': node.name,
                    'docstring': ast.get_docstring(node) or '',
                    'args': [arg.arg for arg in node.args.args],
                    'line_number': node.lineno
                }
                functions.append(function_info)

        return classes, functions

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return [], []

def generate_jekyll_api_page(module_name, classes, functions, output_dir):
    """Generate Jekyll markdown page for API documentation."""

    # Create Jekyll front matter
    content = f"""---
layout: default
title: {module_name} API Reference
nav_order: 2
parent: API Documentation
---

# {module_name} API Reference

"""

    # Add table of contents
    if classes or functions:
        content += "## Table of Contents\n\n"

        if classes:
            content += "### Classes\n"
            for cls in classes:
                content += f"- [{cls['name']}](#{cls['name'].lower()})\n"
            content += "\n"

        if functions:
            content += "### Functions\n"
            for func in functions:
                content += f"- [{func['name']}](#{func['name'].lower()})\n"
            content += "\n"

    # Document classes
    for cls in classes:
        content += f"## {cls['name']}\n\n"

        if cls['docstring']:
            content += f"{cls['docstring']}\n\n"

        # Add interactive link to source
        github_link = f"https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{cls['line_number']}"
        content += f"<div class='source-link'><a href='{github_link}' target='_blank'>📂 View source code</a></div>\n\n"

        if cls['methods']:
            content += "### Methods\n\n"

            for method in cls['methods']:
                if method['name'].startswith('_') and method['name'] != '__init__':
                    continue  # Skip private methods except __init__

                content += f"#### {method['name']}\n\n"

                # Method signature
                args_str = ', '.join(method['args'])
                content += f"```python\n{method['name']}({args_str})\n```\n\n"

                if method['docstring']:
                    content += f"{method['docstring']}\n\n"

                # Link to specific method in source
                method_github_link = f"https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{method['line_number']}"
                content += f"<div class='method-source-link'><a href='{method_github_link}' target='_blank'>📍 View method source</a></div>\n\n"

    # Document top-level functions
    for func in functions:
        content += f"## {func['name']}\n\n"

        # Function signature
        args_str = ', '.join(func['args'])
        content += f"```python\n{func['name']}({args_str})\n```\n\n"

        if func['docstring']:
            content += f"{func['docstring']}\n\n"

        # Link to function in source
        func_github_link = f"https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{func['line_number']}"
        content += f"<div class='source-link'><a href='{func_github_link}' target='_blank'>📂 View source code</a></div>\n\n"

    # Write the file
    output_file = output_dir / f"{module_name.lower()}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated API docs for {module_name}")

def main():
    """Main function to generate all API documentation."""

    # Ensure output directory exists
    api_docs_dir = Path('../api')
    api_docs_dir.mkdir(exist_ok=True)

    # Create main API index page
    index_content = """---
layout: default
title: API Documentation
nav_order: 3
has_children: true
---

# COGITO API Documentation

Complete API reference for the COGITO package.

<div class="api-overview">
    <div class="api-card">
        <h3><a href="cogito.html">COGITO Core</a></h3>
        <p>Main COGITO class for running quantum chemistry analysis</p>
    </div>

    <div class="api-card">
        <h3><a href="cogitopost.html">COGITOpost</a></h3>
        <p>Post-processing tools for band structure and bonding analysis</p>
    </div>

    <div class="api-card">
        <h3><a href="cogitoico.html">COGITOico</a></h3>
        <p>Advanced analysis tools and visualizations</p>
    </div>
</div>

## Quick Links

- [Installation Guide](../tutorial/#COGITO)
- [Basic Tutorial](../tutorial/)
- [Examples](../examples/)

<style>
.api-overview {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin: 20px 0;
}

.api-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    flex: 1;
    min-width: 250px;
    transition: box-shadow 0.3s ease;
}

.api-card:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.api-card h3 {
    margin-top: 0;
}

.api-card a {
    text-decoration: none;
    color: #2c5aa0;
}

.source-link, .method-source-link {
    background: #f8f9fa;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 10px 0;
}

.source-link a, .method-source-link a {
    color: #6f42c1;
    text-decoration: none;
    font-size: 0.9em;
}

.source-link a:hover, .method-source-link a:hover {
    text-decoration: underline;
}
</style>
"""

    with open(api_docs_dir / 'index.md', 'w') as f:
        f.write(index_content)

    # Main COGITO modules to document
    cogito_modules = [
        ('COGITO', '../../COGITO/COGITO.py'),
        ('COGITOpost', '../../COGITO/COGITOpost.py'),
        ('COGITOico', '../../COGITO/COGITOico.py')
    ]

    for module_name, file_path in cogito_modules:
        if os.path.exists(file_path):
            classes, functions = extract_docstring_and_methods(file_path)
            generate_jekyll_api_page(module_name, classes, functions, api_docs_dir)
        else:
            print(f"Warning: {file_path} not found")

if __name__ == "__main__":
    main()