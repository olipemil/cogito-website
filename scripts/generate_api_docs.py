#!/usr/bin/env python3
"""
Generate ReadTheDocs-style API documentation from COGITO source code.
"""

import os
import sys
import re
import ast
import inspect
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Add COGITO to path
sys.path.insert(0, '../../COGITO')

def parse_docstring(docstring: str) -> Dict:
    """Parse docstring into structured format similar to Sphinx."""
    if not docstring:
        return {'description': '', 'parameters': [], 'returns': '', 'raises': [], 'examples': []}

    sections = {
        'description': '',
        'parameters': [],
        'returns': '',
        'raises': [],
        'examples': []
    }

    lines = docstring.strip().split('\n')
    current_section = 'description'
    current_param = None
    description_lines = []

    for line in lines:
        line = line.strip()

        # Check for parameter annotations
        if line.startswith('@param') or line.startswith(':param'):
            # Parse @param name: description or :param name: description
            param_match = re.match(r'[@:]param\s+(\w+):\s*(.*)', line)
            if param_match:
                param_name, param_desc = param_match.groups()
                current_param = {'name': param_name, 'description': param_desc, 'type': ''}
                sections['parameters'].append(current_param)
                current_section = 'param'
            continue

        elif line.startswith('@type') or line.startswith(':type'):
            # Parse @type name: type or :type name: type
            type_match = re.match(r'[@:]type\s+(\w+):\s*(.*)', line)
            if type_match and current_param:
                param_name, param_type = type_match.groups()
                if current_param['name'] == param_name:
                    current_param['type'] = param_type
            continue

        elif line.startswith('@return') or line.startswith(':return') or line.startswith('@returns') or line.startswith(':returns'):
            # Parse return description
            return_match = re.match(r'[@:]returns?:\s*(.*)', line)
            if return_match:
                sections['returns'] = return_match.group(1)
                current_section = 'returns'
            continue

        elif line.startswith('@raises') or line.startswith(':raises'):
            # Parse exception information
            raises_match = re.match(r'[@:]raises\s+(\w+):\s*(.*)', line)
            if raises_match:
                exception_name, exception_desc = raises_match.groups()
                sections['raises'].append({'exception': exception_name, 'description': exception_desc})
                current_section = 'raises'
            continue

        elif line.startswith('Example') or line.startswith('Examples'):
            current_section = 'examples'
            continue

        # Handle continuation lines
        if current_section == 'description':
            if line:
                description_lines.append(line)
        elif current_section == 'param' and current_param and line:
            current_param['description'] += ' ' + line
        elif current_section == 'returns' and line:
            sections['returns'] += ' ' + line
        elif current_section == 'examples' and line:
            sections['examples'].append(line)

    sections['description'] = '\n'.join(description_lines)
    return sections

def extract_function_signature(node: ast.FunctionDef) -> str:
    """Extract clean function signature."""
    args = []

    # Regular arguments
    for arg in node.args.args:
        args.append(arg.arg)

    # Add defaults
    defaults = node.args.defaults
    num_defaults = len(defaults)
    num_args = len(node.args.args)

    if num_defaults > 0:
        # Apply defaults to last n arguments
        for i in range(num_args - num_defaults, num_args):
            if i < len(args):
                # Try to get default value as string
                default_node = defaults[i - (num_args - num_defaults)]
                if isinstance(default_node, ast.Constant):
                    default_val = repr(default_node.value)
                elif isinstance(default_node, ast.Name):
                    default_val = default_node.id
                else:
                    default_val = "..."
                args[i] = f"{args[i]}={default_val}"

    return f"{node.name}({', '.join(args)})"

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
                class_docstring = ast.get_docstring(node) or ''
                parsed_class_doc = parse_docstring(class_docstring)

                class_info = {
                    'name': node.name,
                    'docstring': class_docstring,
                    'parsed_doc': parsed_class_doc,
                    'methods': [],
                    'line_number': node.lineno
                }

                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_docstring = ast.get_docstring(item) or ''
                        parsed_method_doc = parse_docstring(method_docstring)
                        signature = extract_function_signature(item)

                        method_info = {
                            'name': item.name,
                            'signature': signature,
                            'docstring': method_docstring,
                            'parsed_doc': parsed_method_doc,
                            'args': [arg.arg for arg in item.args.args],
                            'line_number': item.lineno
                        }
                        class_info['methods'].append(method_info)

                classes.append(class_info)

            elif isinstance(node, ast.FunctionDef) and node.col_offset == 0:
                # Top-level functions
                function_docstring = ast.get_docstring(node) or ''
                parsed_func_doc = parse_docstring(function_docstring)
                signature = extract_function_signature(node)

                function_info = {
                    'name': node.name,
                    'signature': signature,
                    'docstring': function_docstring,
                    'parsed_doc': parsed_func_doc,
                    'args': [arg.arg for arg in node.args.args],
                    'line_number': node.lineno
                }
                functions.append(function_info)

        return classes, functions

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return [], []

def generate_readthedocs_style_page(module_name, classes, functions, output_dir):
    """Generate ReadTheDocs-style Jekyll markdown page for API documentation."""

    # Create Jekyll front matter
    content = f"""---
layout: default
title: {module_name} API Reference
nav_order: 2
parent: API Documentation
---

# {module_name} API Reference

<div class="api-module-header">
    <p class="module-description">API reference for the {module_name} module</p>
    <div class="source-link">
        <a href="https://github.com/olipemil/COGITO/blob/main/{module_name}.py" target="_blank">View Source</a>
    </div>
</div>

"""

    # Add tabbed interface
    if classes or functions:
        content += """<div class="api-tabs">
    <div class="tab-buttons">"""

        if classes:
            content += '\n        <button class="tab-btn active" onclick="showTab(\'classes\')">Classes</button>'
        if functions:
            content += '\n        <button class="tab-btn" onclick="showTab(\'functions\')">Functions</button>'

        content += """
    </div>
"""

    # Classes tab
    if classes:
        content += """
    <div id="classes" class="tab-content active">
"""
        for cls in classes:
            content += generate_class_documentation(cls, module_name)

        content += "    </div>\n"

    # Functions tab
    if functions:
        content += """
    <div id="functions" class="tab-content">
"""
        for func in functions:
            content += generate_function_documentation(func, module_name)

        content += "    </div>\n"

    if classes or functions:
        content += "</div>\n"

    # Add CSS and JavaScript
    content += generate_readthedocs_styles_and_scripts()

    # Write the file
    output_file = output_dir / f"{module_name.lower()}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated ReadTheDocs-style API docs for {module_name}")

def generate_class_documentation(cls, module_name):
    """Generate documentation for a single class."""
    content = f"""
        <div class="class-section" id="{cls['name'].lower()}">
            <div class="class-header">
                <h2>class {cls['name']}</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{cls['line_number']}" target="_blank">source</a>
                </div>
            </div>
"""

    # Class description
    if cls['parsed_doc']['description']:
        content += f"""
            <div class="class-description">
                <p>{cls['parsed_doc']['description']}</p>
            </div>
"""

    # Class parameters (for __init__)
    init_method = next((m for m in cls['methods'] if m['name'] == '__init__'), None)
    if init_method and init_method['parsed_doc']['parameters']:
        content += generate_parameters_table(init_method['parsed_doc']['parameters'])

    # Methods
    if cls['methods']:
        content += """
            <div class="methods-section">
                <h3>Methods</h3>
                <div class="methods-list">
"""

        for method in cls['methods']:
            if method['name'].startswith('_') and method['name'] != '__init__':
                continue  # Skip private methods except __init__

            content += generate_method_documentation(method, module_name)

        content += """
                </div>
            </div>
"""

    content += "        </div>\n"
    return content

def generate_method_documentation(method, module_name):
    """Generate documentation for a single method."""
    content = f"""
                    <div class="method" id="{method['name']}">
                        <div class="method-header">
                            <h4>{method['name']}</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{method['line_number']}" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>{method['signature']}</code>
                        </div>
"""

    # Method description
    if method['parsed_doc']['description']:
        content += f"""
                        <div class="method-description">
                            <p>{method['parsed_doc']['description']}</p>
                        </div>
"""

    # Parameters
    if method['parsed_doc']['parameters']:
        content += generate_parameters_table(method['parsed_doc']['parameters'])

    # Returns
    if method['parsed_doc']['returns']:
        content += f"""
                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>{method['parsed_doc']['returns']}</p>
                        </div>
"""

    # Raises
    if method['parsed_doc']['raises']:
        content += """
                        <div class="raises-section">
                            <h5>Raises</h5>
                            <ul>
"""
        for raise_info in method['parsed_doc']['raises']:
            content += f"                                <li><strong>{raise_info['exception']}</strong>: {raise_info['description']}</li>\n"

        content += """                            </ul>
                        </div>
"""

    # Examples
    if method['parsed_doc']['examples']:
        content += """
                        <div class="examples-section">
                            <h5>Examples</h5>
                            <pre><code>
"""
        content += '\n'.join(method['parsed_doc']['examples'])
        content += """
                            </code></pre>
                        </div>
"""

    content += "                    </div>\n"
    return content

def generate_function_documentation(func, module_name):
    """Generate documentation for a top-level function."""
    content = f"""
        <div class="function-section" id="{func['name'].lower()}">
            <div class="function-header">
                <h2>{func['name']}</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/{module_name}.py#L{func['line_number']}" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>{func['signature']}</code>
            </div>
"""

    # Function description
    if func['parsed_doc']['description']:
        content += f"""
            <div class="function-description">
                <p>{func['parsed_doc']['description']}</p>
            </div>
"""

    # Parameters
    if func['parsed_doc']['parameters']:
        content += generate_parameters_table(func['parsed_doc']['parameters'])

    # Returns
    if func['parsed_doc']['returns']:
        content += f"""
            <div class="returns-section">
                <h4>Returns</h4>
                <p>{func['parsed_doc']['returns']}</p>
            </div>
"""

    # Examples
    if func['parsed_doc']['examples']:
        content += """
            <div class="examples-section">
                <h4>Examples</h4>
                <pre><code>
"""
        content += '\n'.join(func['parsed_doc']['examples'])
        content += """
                </code></pre>
            </div>
"""

    content += "        </div>\n"
    return content

def generate_parameters_table(parameters):
    """Generate a parameters table in ReadTheDocs style."""
    if not parameters:
        return ""

    content = """
                        <div class="parameters-section">
                            <h5>Parameters</h5>
                            <table class="parameters-table">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Type</th>
                                        <th>Description</th>
                                    </tr>
                                </thead>
                                <tbody>
"""

    for param in parameters:
        param_type = param.get('type', '') or 'Any'
        content += f"""                                    <tr>
                                        <td><code>{param['name']}</code></td>
                                        <td><code>{param_type}</code></td>
                                        <td>{param['description']}</td>
                                    </tr>
"""

    content += """                                </tbody>
                            </table>
                        </div>
"""
    return content

def generate_readthedocs_styles_and_scripts():
    """Generate ReadTheDocs-style CSS and JavaScript."""
    return """
<!-- ReadTheDocs-style CSS -->
<style>
.api-module-header {
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 20px;
    margin-bottom: 30px;
}

.module-description {
    color: #666;
    font-size: 16px;
    margin: 10px 0;
}

.api-tabs {
    margin: 20px 0;
}

.tab-buttons {
    border-bottom: 1px solid #ddd;
    margin-bottom: 20px;
}

.tab-btn {
    background: none;
    border: none;
    padding: 12px 20px;
    cursor: pointer;
    font-size: 14px;
    color: #666;
    border-bottom: 3px solid transparent;
    margin-right: 10px;
    transition: all 0.3s ease;
}

.tab-btn.active {
    color: #2c5aa0;
    border-bottom-color: #2c5aa0;
    font-weight: 600;
}

.tab-btn:hover {
    color: #2c5aa0;
}

.tab-content {
    display: none;
}

.tab-content.active {
    display: block;
}

.class-section, .function-section {
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin-bottom: 30px;
    overflow: hidden;
}

.class-header, .function-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.class-header h2, .function-header h2 {
    margin: 0;
    font-size: 20px;
    color: #2c5aa0;
    font-weight: 600;
}

.class-description, .function-description {
    padding: 20px;
    background: white;
    border-bottom: 1px solid #f0f0f0;
}

.methods-section {
    background: white;
}

.methods-section h3 {
    margin: 0;
    padding: 16px 20px;
    background: #f8f9fa;
    border-bottom: 1px solid #e1e4e8;
    font-size: 16px;
    color: #2c5aa0;
}

.methods-list {
    padding: 0;
}

.method {
    border-bottom: 1px solid #f0f0f0;
    padding: 20px;
}

.method:last-child {
    border-bottom: none;
}

.method-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}

.method-header h4 {
    margin: 0;
    font-size: 16px;
    color: #2c5aa0;
    font-weight: 600;
}

.signature {
    background: #f6f8fa;
    padding: 12px 16px;
    border-radius: 6px;
    border: 1px solid #e1e4e8;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.method-description, .function-description p {
    margin: 12px 0;
    line-height: 1.6;
    color: #333;
}

.parameters-section, .returns-section, .raises-section, .examples-section {
    margin: 16px 0;
}

.parameters-section h5, .returns-section h5, .raises-section h5, .examples-section h5,
.returns-section h4, .examples-section h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.parameters-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 14px;
}

.parameters-table th {
    background: #f6f8fa;
    padding: 12px;
    text-align: left;
    border: 1px solid #e1e4e8;
    font-weight: 600;
    color: #2c5aa0;
    font-size: 13px;
}

.parameters-table td {
    padding: 12px;
    border: 1px solid #e1e4e8;
    vertical-align: top;
}

.parameters-table code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #2c5aa0;
}

.source-link {
    font-size: 12px;
}

.source-link a {
    color: #666;
    text-decoration: none;
    background: #f0f0f0;
    padding: 4px 8px;
    border-radius: 3px;
    transition: all 0.2s ease;
}

.source-link a:hover {
    background: #e0e0e0;
    color: #2c5aa0;
}

.raises-section ul {
    margin: 8px 0;
    padding-left: 20px;
}

.raises-section li {
    margin: 4px 0;
}

.examples-section pre {
    background: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    border: 1px solid #e1e4e8;
    overflow-x: auto;
    margin: 8px 0;
}

.examples-section code {
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    color: #333;
}
</style>

<!-- ReadTheDocs-style JavaScript -->
<script>
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab content
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }

    // Add active class to clicked button
    event.target.classList.add('active');
}

// Initialize first tab as active on page load
document.addEventListener('DOMContentLoaded', function() {
    const firstTabButton = document.querySelector('.tab-btn');
    const firstTabContent = document.querySelector('.tab-content');

    if (firstTabButton && firstTabContent) {
        firstTabButton.classList.add('active');
        firstTabContent.classList.add('active');
    }
});
</script>
"""

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
            generate_readthedocs_style_page(module_name, classes, functions, api_docs_dir)
        else:
            print(f"Warning: {file_path} not found")

if __name__ == "__main__":
    main()