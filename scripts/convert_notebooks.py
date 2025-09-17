#!/usr/bin/env python3
"""
Convert Jupyter notebooks to Jekyll-compatible markdown pages with custom styling.
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def embed_notebook_in_jekyll(notebook_path, output_dir, template_vars=None):
    """Create Jekyll page that embeds the actual Jupyter notebook."""

    if template_vars is None:
        template_vars = {}

    notebook_name = Path(notebook_path).stem
    notebook_filename = Path(notebook_path).name

    # Extract title from first markdown cell or use filename
    title = template_vars.get('title', notebook_name.replace('_', ' ').title())

    # GitHub raw URL for the notebook
    github_notebook_url = f"https://raw.githubusercontent.com/olipemil/COGITO/main/COGITO_paper/{notebook_filename}"
    github_view_url = f"https://github.com/olipemil/COGITO/blob/main/COGITO_paper/{notebook_filename}"
    nbviewer_url = f"https://nbviewer.org/github/olipemil/COGITO/blob/main/COGITO_paper/{notebook_filename}"

    # Create Jekyll page that embeds the notebook
    jekyll_content = f"""---
layout: default
title: {title}
parent: Examples
nav_order: {template_vars.get('nav_order', 1)}
---

# {title}

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Interactive Jupyter notebook example</p>
        <div class="notebook-buttons">
            <a href="{nbviewer_url}" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="{github_view_url}" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="{github_notebook_url}" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

<div class="jupyter-notebook">
    <iframe
        src="{nbviewer_url}"
        width="100%"
        height="800"
        frameborder="0"
        title="{title} Jupyter Notebook">
    </iframe>
</div>

<!-- Fallback for if iframe doesn't work -->
<div class="notebook-fallback" style="display: none;">
    <div class="fallback-message">
        <h3>🔧 Notebook Display</h3>
        <p>If the notebook doesn't display above, you can:</p>
        <ul>
            <li><a href="{nbviewer_url}" target="_blank">View in NBViewer</a> (recommended)</li>
            <li><a href="{github_view_url}" target="_blank">View on GitHub</a></li>
            <li><a href="{github_notebook_url}" download>Download and run locally</a></li>
        </ul>
    </div>
</div>

<style>
.notebook-controls {{
    margin: 20px 0;
}}

.notebook-info {{
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
}}

.notebook-info p {{
    margin: 0 0 10px 0;
    font-weight: 500;
}}

.notebook-buttons {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.btn {{
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
    display: inline-block;
}}

.btn-primary {{
    background: #2c5aa0;
    color: white;
}}

.btn-primary:hover {{
    background: #1a365d;
    color: white;
}}

.btn-secondary {{
    background: #6c757d;
    color: white;
}}

.btn-secondary:hover {{
    background: #545b62;
    color: white;
}}

.btn-success {{
    background: #28a745;
    color: white;
}}

.btn-success:hover {{
    background: #1e7e34;
    color: white;
}}

.jupyter-notebook {{
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px 0;
}}

.jupyter-notebook iframe {{
    width: 100%;
    min-height: 600px;
    border: none;
}}

.fallback-message {{
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}}

.fallback-message h3 {{
    margin-top: 0;
    color: #856404;
}}

.fallback-message ul {{
    margin-bottom: 0;
}}

.fallback-message a {{
    color: #856404;
    font-weight: 500;
}}

/* Responsive design */
@media (max-width: 768px) {{
    .notebook-buttons {{
        flex-direction: column;
    }}

    .jupyter-notebook iframe {{
        height: 600px;
    }}
}}
</style>

<script>
// Show fallback if iframe fails to load
document.addEventListener('DOMContentLoaded', function() {{
    const iframe = document.querySelector('.jupyter-notebook iframe');
    const fallback = document.querySelector('.notebook-fallback');

    iframe.addEventListener('error', function() {{
        fallback.style.display = 'block';
    }});

    // Check if iframe loaded successfully after some time
    setTimeout(function() {{
        try {{
            if (!iframe.contentDocument && !iframe.contentWindow) {{
                fallback.style.display = 'block';
            }}
        }} catch (e) {{
            // Cross-origin restrictions might trigger this
            console.log('Iframe loaded (cross-origin)');
        }}
    }}, 3000);
}});
</script>
"""

    # Write the Jekyll file
    output_file = output_dir / f"{notebook_name}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(jekyll_content)

    print(f"Created embedded notebook page: {output_file}")

    return output_file

def create_examples_index():
    """Create the main examples index page."""

    examples_dir = Path('../examples')
    examples_dir.mkdir(exist_ok=True)

    index_content = """---
layout: default
title: Examples
nav_order: 4
has_children: true
---

# COGITO Examples

Interactive Jupyter notebook examples demonstrating COGITO's capabilities.

<div class="examples-grid">
    <div class="example-card">
        <h3><a href="cogito_example.html">COGITO Example</a></h3>
        <p>Complete walkthrough of COGITO analysis workflow</p>
        <div class="example-tags">
            <span class="tag">Band Structure</span>
            <span class="tag">Orbital Analysis</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="basic_installation_and_setup.html">Installation & Setup</a></h3>
        <p>Get started with COGITO installation and basic configuration</p>
        <div class="example-tags">
            <span class="tag">Getting Started</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="band_structure_analysis.html">Band Structure Analysis</a></h3>
        <p>Advanced band structure analysis and visualization</p>
        <div class="example-tags">
            <span class="tag">Band Structure</span>
            <span class="tag">Visualization</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="cohp_coop_analysis.html">COHP/COOP Analysis</a></h3>
        <p>Chemical bonding analysis using COHP and COOP</p>
        <div class="example-tags">
            <span class="tag">Bonding</span>
            <span class="tag">COHP</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="crystal_bonding_visualization.html">Crystal Bonding</a></h3>
        <p>3D visualization of crystal structures with bonding</p>
        <div class="example-tags">
            <span class="tag">3D Visualization</span>
            <span class="tag">Crystal Structure</span>
        </div>
    </div>
</div>

## Getting Started

1. **[Download examples](https://github.com/olipemil/COGITO/tree/main/examples)** from the COGITO repository
2. **Install dependencies** using the [installation guide](../tutorial/#COGITO)
3. **Run notebooks** in your local Jupyter environment

<div class="getting-started-note">
💡 <strong>Tip:</strong> All examples are designed to work with the sample data included in the COGITO repository.
</div>

<style>
.examples-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin: 30px 0;
}

.example-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    transition: all 0.3s ease;
    background: white;
}

.example-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}

.example-card h3 {
    margin-top: 0;
    margin-bottom: 10px;
}

.example-card h3 a {
    text-decoration: none;
    color: #2c5aa0;
}

.example-card h3 a:hover {
    text-decoration: underline;
}

.example-card p {
    color: #666;
    margin-bottom: 15px;
}

.example-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    background: #e9ecef;
    color: #495057;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.85em;
    font-weight: 500;
}

.getting-started-note {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    border-radius: 4px;
    padding: 15px;
    margin: 20px 0;
}
</style>
"""

    with open(examples_dir / 'index.md', 'w') as f:
        f.write(index_content)

def main():
    """Main function to embed all notebooks."""

    # Create examples directory
    examples_dir = Path('../examples')
    examples_dir.mkdir(exist_ok=True)

    # Create examples index
    create_examples_index()

    # Embed existing COGITO example notebook
    cogito_notebook = '../../COGITO/COGITO_paper/COGITO_example.ipynb'
    if os.path.exists(cogito_notebook):
        embed_notebook_in_jekyll(
            cogito_notebook,
            examples_dir,
            {
                'title': 'COGITO Example Workflow',
                'nav_order': 1
            }
        )
    else:
        # Create a placeholder that links to the notebook
        create_notebook_placeholder(
            'COGITO_example',
            'COGITO Example Workflow',
            examples_dir,
            'COGITO_paper/COGITO_example.ipynb',
            1
        )

    # Convert other example notebooks from COGITO/examples if they exist
    cogito_examples_dir = Path('../../COGITO/examples')
    if cogito_examples_dir.exists():
        nav_order = 2
        for notebook_file in cogito_examples_dir.glob('*.ipynb'):
            embed_notebook_in_jekyll(
                notebook_file,
                examples_dir,
                {
                    'title': notebook_file.stem.replace('_', ' ').title(),
                    'nav_order': nav_order
                }
            )
            nav_order += 1

    print("Notebook embedding completed!")

def create_notebook_placeholder(notebook_name, title, output_dir, github_path, nav_order):
    """Create a placeholder page that links to a notebook on GitHub."""

    github_notebook_url = f"https://raw.githubusercontent.com/olipemil/COGITO/main/{github_path}"
    github_view_url = f"https://github.com/olipemil/COGITO/blob/main/{github_path}"
    nbviewer_url = f"https://nbviewer.org/github/olipemil/COGITO/blob/main/{github_path}"

    content = f"""---
layout: default
title: {title}
parent: Examples
nav_order: {nav_order}
---

# {title}

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Interactive Jupyter notebook example</p>
        <div class="notebook-buttons">
            <a href="{nbviewer_url}" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="{github_view_url}" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="{github_notebook_url}" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

<div class="jupyter-notebook">
    <iframe
        src="{nbviewer_url}"
        width="100%"
        height="800"
        frameborder="0"
        title="{title} Jupyter Notebook">
    </iframe>
</div>

<style>
.notebook-controls {{
    margin: 20px 0;
}}

.notebook-info {{
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
}}

.notebook-buttons {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.btn {{
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
    display: inline-block;
}}

.btn-primary {{
    background: #2c5aa0;
    color: white;
}}

.btn-primary:hover {{
    background: #1a365d;
    color: white;
}}

.btn-secondary {{
    background: #6c757d;
    color: white;
}}

.btn-secondary:hover {{
    background: #545b62;
    color: white;
}}

.btn-success {{
    background: #28a745;
    color: white;
}}

.btn-success:hover {{
    background: #1e7e34;
    color: white;
}}

.jupyter-notebook {{
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px 0;
}}

.jupyter-notebook iframe {{
    width: 100%;
    min-height: 600px;
    border: none;
}}
</style>
"""

    output_file = output_dir / f"{notebook_name}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created notebook placeholder: {output_file}")

if __name__ == "__main__":
    main()