# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add COGITO to path
sys.path.insert(0, os.path.abspath('../../../COGITO'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'COGITO API'
copyright = '2025, COGITO Team'
author = 'COGITO Team'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings
    'sphinx_markdown_builder',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Autodoc configuration --------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Show both the class docstring and __init__ docstring
autodoc_class_signature = 'mixed'

# -- Napoleon configuration -------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Custom docstring preprocessing to handle @param format ----------------
def process_docstring(app, what, name, obj, options, lines):
    """Convert @param format to :param format for Sphinx parsing."""
    for i, line in enumerate(lines):
        # Convert @param name: description to :param name: description
        if line.strip().startswith('@param '):
            lines[i] = line.replace('@param ', ':param ')
        # Convert @return: description to :returns: description
        elif line.strip().startswith('@return'):
            lines[i] = line.replace('@return', ':returns')
        # Convert @raises to :raises
        elif line.strip().startswith('@raises '):
            lines[i] = line.replace('@raises ', ':raises ')

def add_readthedocs_css_to_markdown():
    """Add ReadTheDocs-style CSS to generated markdown files."""

    css_content = """---
layout: default
title: {{title}}
nav_order: {{nav_order}}
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

"""

    return css_content

def post_process_markdown_files():
    """Post-process generated markdown files to add ReadTheDocs styling."""
    import os
    from pathlib import Path

    api_sphinx_dir = Path('../api-sphinx')

    # File mapping for navigation order
    file_mapping = {
        'cogito.md': {'title': 'COGITO Core API Reference', 'nav_order': 2},
        'cogitopost.md': {'title': 'COGITOpost API Reference', 'nav_order': 3},
        'cogitoico.md': {'title': 'COGITOico API Reference', 'nav_order': 4},
        'index.md': {'title': 'API Documentation', 'nav_order': 1}
    }

    if api_sphinx_dir.exists():
        for md_file in api_sphinx_dir.glob('*.md'):
            if md_file.name in file_mapping:
                file_info = file_mapping[md_file.name]

                # Read original content
                content = md_file.read_text()

                # Add CSS and Jekyll front matter
                css_header = add_readthedocs_css_to_markdown().replace(
                    '{{title}}', file_info['title']
                ).replace(
                    '{{nav_order}}', str(file_info['nav_order'])
                )

                # Write updated content
                new_content = css_header + content
                md_file.write_text(new_content)

                print(f"Added ReadTheDocs CSS to {md_file.name}")

def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect('build-finished', lambda app, exception: post_process_markdown_files())

# -- Markdown builder configuration -----------------------------------------
markdown_http_base = 'https://olipemil.github.io/cogito-website'
markdown_uri_doc_suffix = '.html'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
