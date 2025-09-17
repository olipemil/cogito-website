---
layout: default
title: Basic Analysis
parent: Examples
nav_order: 2
---

# Basic Analysis

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Core COGITO analysis workflows - verification and band structure</p>
        <div class="notebook-buttons">
            <a href="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="https://github.com/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="https://raw.githubusercontent.com/olipemil/cogito-website/make_new/examples/COGITO_tutorial_actual.ipynb" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

## What You'll Learn

- **Quality Verification**: Check COGITO model accuracy against DFT
- **Parameter Analysis**: Understand hopping and overlap decay
- **Band Structure**: Generate and analyze electronic band structure
- **Validation**: Compare COGITO results with original VASP calculations

<div class="jupyter-notebook">
    <iframe
        src="https://nbviewer.org/github/olipemil/cogito-website/blob/make_new/examples/COGITO_tutorial_actual.ipynb"
        width="100%"
        height="800"
        frameborder="0"
        title="COGITO Basic Analysis Tutorial">
    </iframe>
</div>

## Key Analysis Steps

### 1. Model Verification

```python
from COGITOpost import COGITO_analyze as coze

# Initialize analysis
COGITOTB = coze(direct, min_hopping_dist=15, min_overlap_dist=15)

# Compare with DFT
COGITOTB.compare_to_DFT(direct)
```

### 2. Parameter Quality Check

```python
# Check parameter decay
COGITOTB.plot_hopping()
COGITOTB.plot_overlaps()
```

### 3. Band Structure Generation

```python
# Generate band structure
COGITOTB.get_bandstructure(num_kpts=15)
COGITOTB.plotBS(ylim=(-12, 20))
```

## What to Look For

- **DFT Comparison**: Small errors indicate good COGITO quality
- **Parameter Decay**: Should show linear decay on log scale
- **Band Structure**: Should match DFT bands within expected tolerance

## Next Steps

- [**Advanced Features**](advanced_features.html) - Explore COHP analysis and crystal bonding
- [**Installation & Setup**](installation_setup.html) - Review setup if needed

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