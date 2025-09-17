---
layout: default
title: Advanced Features
parent: Examples
nav_order: 3
---

# Advanced Features

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Chemical bonding analysis, COHP/COOP, and crystal visualization</p>
        <div class="notebook-buttons">
            <a href="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="https://github.com/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="https://raw.githubusercontent.com/olipemil/cogito-website/make_new/examples/COGITO_tutorial_actual.ipynb" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

## What You'll Learn

- **COHP Analysis**: Crystal Orbital Hamilton Population analysis
- **Chemical Bonding**: Understand bonding vs antibonding contributions
- **Charge Analysis**: Atomic charge partitioning and electron distribution
- **3D Visualization**: Visualize covalent bonds in crystal structures

<div class="jupyter-notebook">
    <iframe
        src="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb"
        width="100%"
        height="800"
        frameborder="0"
        title="COGITO Advanced Features Tutorial">
    </iframe>
</div>

## Key Advanced Features

### 1. COHP on Band Structure

```python
# Define orbital sets for analysis
orbs_dict = [{"Si":["s","p"]}, {"Si":["s","p"]}]

# Generate COHP analysis
COGITOTB.get_COHP("BS", orbs_dict, NN=2, ylim=(-12,5))
```

### 2. Uniform Grid Analysis

```python
# Switch to uniform k-point grid
COGITOTB.get_uniform((5,5,5))

# Analyze electron distribution
# This shows where electrons are located
```

### 3. COHP on Density of States

```python
# COHP analysis on DOS
COGITOTB.get_COHP("DOS", orbs_dict, NN=1, sigma=0.1, ylim=(-15,1))
```

### 4. Crystal Bond Visualization

```python
# Visualize actual covalent bonds in 3D
COGITOTB.get_bonds_figure(energy_cutoff=0.1)
```

## Understanding COHP Results

- **Positive values**: Bonding interactions (stabilizing)
- **Negative values**: Antibonding interactions (destabilizing)
- **Energy cutoff**: Determines which bonds are shown in visualization
- **NN parameter**: Controls nearest neighbor interactions

## Interactive Features

- **Dash App**: Create interactive COHP analysis interface
- **3D Bonds**: Rotate and explore crystal structures
- **Hover Data**: Get detailed information about specific bonds

## Related Documentation

- [**API: get_COHP**](../api/cogitopost.html#get_cohp) - Full COHP analysis options
- [**API: get_bonds_figure**](../api/cogitopost.html#get_bonds_figure) - 3D visualization parameters
- [**Tutorial: Uniform Analysis**](../tutorial/#uniform) - Detailed uniform grid workflow

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