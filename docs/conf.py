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

# Show type hints in signature
autodoc_typehints = 'description'
autodoc_class_signature = 'mixed'

# -- Napoleon configuration for Google-style docstrings --------------------
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

# Custom docstring processing for better formatting
def process_docstring(app, what, name, obj, options, lines):
    """Process docstrings to improve formatting."""
    result = []
    for line in lines:
        # Improve parameter formatting
        if line.strip().startswith('Args:') or line.strip().startswith('Arguments:'):
            result.append('**Parameters:**')
        elif line.strip().startswith('Returns:'):
            result.append('**Returns:**')
        elif line.strip().startswith('Raises:'):
            result.append('**Raises:**')
        elif line.strip().startswith('Note:'):
            result.append('**Note:**')
        elif line.strip().startswith('Example:') or line.strip().startswith('Examples:'):
            result.append('**Example:**')
        else:
            result.append(line)
    lines[:] = result

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