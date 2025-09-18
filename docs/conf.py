# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add COGITO_sample to path
sys.path.insert(0, os.path.abspath('../COGITO_sample'))

# -- Project information -----------------------------------------------------
project = 'COGITO'
copyright = '2025, COGITO Team'
author = 'COGITO Team'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_markdown_builder',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Autodoc configuration --------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Show type hints in signature only, not in docstring
autodoc_typehints = 'signature'
autodoc_class_signature = 'mixed'
autodoc_preserve_defaults = True

# -- Napoleon configuration for Google-style docstrings --------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Custom docstring processor to handle poorly formatted Google-style docstrings
def process_docstring(app, what, name, obj, options, lines):
    """Clean up docstring indentation issues and convert to proper Google style."""
    if not lines:
        return

    new_lines = []
    in_args = False
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Find Args: section
        if 'Args:' in stripped:
            new_lines.append('Args:')
            in_args = True
            i += 1
            continue

        # Process parameter lines within Args section
        if in_args and stripped:
            # Check if line contains parameter info (name and type)
            if ':' in stripped and '(' in stripped and ')' in stripped:
                # Parse parameter line like "directory (str): The path for the input files"
                try:
                    param_and_type = stripped.split(':')[0].strip()
                    description = ':'.join(stripped.split(':')[1:]).strip()

                    if '(' in param_and_type:
                        param_name = param_and_type.split('(')[0].strip()
                        # Add proper indentation for Google style
                        new_lines.append(f'    {param_name}: {description}')
                    else:
                        new_lines.append(f'    {stripped}')
                except:
                    new_lines.append(f'    {stripped}')
            elif stripped.startswith('Returns:') or stripped.startswith('Note:'):
                in_args = False
                new_lines.append('')
                new_lines.append(stripped)
            elif stripped and not stripped.startswith('"""'):
                new_lines.append(f'    {stripped}')
        else:
            if stripped.startswith('Returns:') or stripped.startswith('Note:'):
                in_args = False
            new_lines.append(line)

        i += 1

    lines[:] = new_lines

def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)

# -- Markdown builder configuration -----------------------------------------
markdown_http_base = 'https://olipemil.github.io/cogito-website'
markdown_uri_doc_suffix = '.html'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'style_nav_header_background': '#2c5aa0',
}