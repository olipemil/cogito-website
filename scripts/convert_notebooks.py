#!/usr/bin/env python3
"""
Convert Jupyter notebooks to Jekyll-compatible markdown pages with custom styling.
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def convert_notebook_to_jekyll(notebook_path, output_dir, template_vars=None):
    """Convert a Jupyter notebook to Jekyll markdown with custom styling."""

    if template_vars is None:
        template_vars = {}

    notebook_name = Path(notebook_path).stem

    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Extract title from first markdown cell or use filename
        title = template_vars.get('title', notebook_name.replace('_', ' ').title())

        # Create Jekyll front matter
        front_matter = f"""---
layout: default
title: {title}
parent: Examples
nav_order: {template_vars.get('nav_order', 1)}
---

# {title}

<div class="notebook-info">
    <p>📓 Interactive Jupyter notebook example</p>
    <p>🔗 <a href="https://github.com/olipemil/COGITO/blob/main/COGITO_paper/{notebook_name}.ipynb" target="_blank">View on GitHub</a></p>
    <p>⬇️ <a href="https://raw.githubusercontent.com/olipemil/COGITO/main/COGITO_paper/{notebook_name}.ipynb" download>Download notebook</a></p>
</div>

"""

        markdown_content = front_matter

        cell_count = 0
        for cell in notebook.get('cells', []):
            cell_count += 1

            if cell['cell_type'] == 'markdown':
                # Process markdown cells
                source = ''.join(cell.get('source', []))
                markdown_content += f"{source}\n\n"

            elif cell['cell_type'] == 'code':
                # Process code cells
                source = ''.join(cell.get('source', []))

                if source.strip():  # Only add non-empty code cells
                    markdown_content += f"<div class='code-cell'>\n\n"
                    markdown_content += f"```python\n{source}\n```\n\n"

                    # Add outputs if they exist
                    outputs = cell.get('outputs', [])
                    if outputs:
                        markdown_content += "<div class='cell-output'>\n\n"

                        for output in outputs:
                            if output.get('output_type') == 'stream':
                                # Text output
                                text = ''.join(output.get('text', []))
                                if text.strip():
                                    markdown_content += f"```\n{text}\n```\n\n"

                            elif output.get('output_type') == 'execute_result' or output.get('output_type') == 'display_data':
                                # Check for image outputs
                                data = output.get('data', {})

                                if 'image/png' in data:
                                    # Handle embedded images
                                    img_data = data['image/png']
                                    markdown_content += f"<img src='data:image/png;base64,{img_data}' alt='Output plot' class='notebook-plot'/>\n\n"

                                elif 'text/plain' in data:
                                    # Handle text outputs
                                    text = ''.join(data['text/plain'])
                                    if text.strip():
                                        markdown_content += f"```\n{text}\n```\n\n"

                        markdown_content += "</div>\n\n"

                    markdown_content += "</div>\n\n"

        # Add custom CSS styling
        styling = """
<style>
.notebook-info {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 15px;
    margin: 20px 0;
}

.notebook-info p {
    margin: 5px 0;
}

.code-cell {
    background: #f8f8f8;
    border-left: 4px solid #2c5aa0;
    padding: 15px;
    margin: 20px 0;
    border-radius: 4px;
}

.cell-output {
    background: #fff;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 10px;
    margin-top: 10px;
}

.notebook-plot {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 10px auto;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.notebook-plot:hover {
    transform: scale(1.02);
    transition: transform 0.3s ease;
}

/* Code highlighting improvements */
.code-cell pre {
    background: transparent;
    border: none;
    margin: 0;
}

.code-cell code {
    background: transparent;
}
</style>
"""

        markdown_content += styling

        # Write the converted file
        output_file = output_dir / f"{notebook_name}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Converted {notebook_name}.ipynb to {output_file}")

    except Exception as e:
        print(f"Error converting {notebook_path}: {e}")

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
    """Main function to convert all notebooks."""

    # Create examples directory
    examples_dir = Path('../examples')
    examples_dir.mkdir(exist_ok=True)

    # Create examples index
    create_examples_index()

    # Convert existing COGITO example notebook
    cogito_notebook = '../../COGITO/COGITO_paper/COGITO_example.ipynb'
    if os.path.exists(cogito_notebook):
        convert_notebook_to_jekyll(
            cogito_notebook,
            examples_dir,
            {
                'title': 'COGITO Example Workflow',
                'nav_order': 1
            }
        )

    # Convert other example notebooks from COGITO/examples if they exist
    cogito_examples_dir = Path('../../COGITO/examples')
    if cogito_examples_dir.exists():
        for notebook_file in cogito_examples_dir.glob('*.ipynb'):
            convert_notebook_to_jekyll(
                notebook_file,
                examples_dir,
                {
                    'title': notebook_file.stem.replace('_', ' ').title(),
                    'nav_order': 2
                }
            )

    print("Notebook conversion completed!")

if __name__ == "__main__":
    main()