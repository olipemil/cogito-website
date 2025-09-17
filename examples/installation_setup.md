---
layout: default
title: Installation & Setup
parent: Examples
nav_order: 1
---

# Installation & Setup

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Learn how to install COGITO and set up your environment</p>
        <div class="notebook-buttons">
            <a href="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="https://github.com/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="https://raw.githubusercontent.com/olipemil/cogito-website/make_new/examples/COGITO_tutorial_actual.ipynb" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

## What You'll Learn

- **Package Installation**: Install all required Python dependencies
- **COGITO Setup**: Set up the COGITO environment
- **VASP File Requirements**: Understand what VASP outputs you need
- **Basic Configuration**: Get ready for your first COGITO analysis

<div class="jupyter-notebook">
    <iframe
        src="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb"
        width="100%"
        height="800"
        frameborder="0"
        title="COGITO Installation & Setup Tutorial">
    </iframe>
</div>

## Quick Start Summary

After installation, you'll be able to run:

```python
from COGITOmain import COGITO

# Initialize with your VASP calculation directory
direct = "path/to/your/vasp/calculation/"
COGITOmodel = COGITO(direct)

# Generate the tight binding model
COGITOmodel.generate_TBmodel(verbose=0, plot_orbs=True)
```

## Next Steps

- [**Basic Analysis**](basic_analysis.html) - Learn core COGITO analysis workflows
- [**Advanced Features**](advanced_features.html) - Explore bonding analysis and visualization

<style>
.notebook-controls {
    margin: 20px 0;
}

.notebook-info {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
}

.notebook-info p {
    margin: 0 0 10px 0;
    font-weight: 500;
}

.notebook-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.btn {
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
    display: inline-block;
}

.btn-primary {
    background: #2c5aa0;
    color: white;
}

.btn-primary:hover {
    background: #1a365d;
    color: white;
}

.btn-secondary {
    background: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background: #545b62;
    color: white;
}

.btn-success {
    background: #28a745;
    color: white;
}

.btn-success:hover {
    background: #1e7e34;
    color: white;
}

.jupyter-notebook {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px 0;
}

.jupyter-notebook iframe {
    width: 100%;
    min-height: 600px;
    border: none;
}

/* Responsive design */
@media (max-width: 768px) {
    .notebook-buttons {
        flex-direction: column;
    }

    .jupyter-notebook iframe {
        height: 600px;
    }
}
</style>