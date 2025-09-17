---
layout: default
title: Band Structure Analysis
parent: Examples
nav_order: 3
---

# Band Structure Analysis

<div class="notebook-info">
    <p>📓 Advanced band structure analysis with COGITO</p>
    <p>🔗 <a href="../api/cogitopost.html#cogito_band">API: COGITO_BAND</a></p>
    <p>📖 <a href="../tutorial/#bandstruc">Tutorial Section</a></p>
</div>

## Overview

This example demonstrates how to:
- Create high-symmetry k-point paths
- Generate band structure plots
- Analyze orbital projections
- Visualize COHP/COOP data

## Setting Up the Band Structure Class

<div class='code-cell'>

```python
# Import required modules
from COGITOpost import COGITO_TB_Model as CoTB
from COGITOpost import COGITO_BAND as CoBS
import matplotlib.pyplot as plt

# Create TB class instance first
direct = "Si/"  # Your calculation directory
my_CoTB = CoTB(direct)

# Restrict parameters for better performance
my_CoTB.restrict_params(maximum_dist=15, minimum_value=0.00001)

print("✅ Tight binding model created successfully")
```

<div class='cell-output'>

```
✅ Tight binding model created successfully
```

</div>

</div>

## Generate Band Structure

<div class='code-cell'>

```python
# Create band structure with high-symmetry path
my_CoBS = CoBS(my_CoTB, num_kpts=10)  # num_kpts per line segment

# Plot basic band structure
my_CoBS.plotBS()

print("📊 Band structure plot generated: band_structure.png")
```

<div class='cell-output'>

```
📊 Band structure plot generated: band_structure.png
```

</div>

</div>

## Orbital Projected Band Structure

<div class='code-cell'>

```python
# Project onto specific orbitals
# For Silicon: s, p, d orbitals
orbital_projections = {"Si": ["s"]}  # Focus on s orbitals

my_CoBS.get_projectedBS(orbital_projections)

print("🎯 Orbital projected band structure created")
print("📁 Output: projectedBS.html (interactive plot)")
```

<div class='cell-output'>

```
🎯 Orbital projected band structure created
📁 Output: projectedBS.html (interactive plot)
```

</div>

</div>

## COHP Analysis

<div class='code-cell'>

```python
# Define orbital sets for COHP analysis
# COHP between all Si orbitals
orbs_dict = [
    {"Si": ["s", "p", "d"]},  # Set 1: All Si orbitals
    {"Si": ["s", "p", "d"]}   # Set 2: All Si orbitals
]

# Generate COHP plot
my_CoBS.get_COHP(orbs_dict)

print("🔬 COHP analysis completed")
print("📁 Output: COHP_BS.html (interactive plot)")
```

<div class='cell-output'>

```
🔬 COHP analysis completed
📁 Output: COHP_BS.html (interactive plot)
```

</div>

</div>

## Interactive COHP Dashboard

<div class='code-cell'>

```python
# Launch interactive dashboard for COHP exploration
# This creates a web interface for dynamic COHP analysis

print("🚀 Launching interactive COHP dashboard...")
print("💡 This will open a web interface at http://127.0.0.1:8050/")

# Uncomment to run:
# my_CoBS.make_COHP_dashapp()
```

<div class='cell-output'>

```
🚀 Launching interactive COHP dashboard...
💡 This will open a web interface at http://127.0.0.1:8050/
```

</div>

</div>

## Advanced Analysis

<div class='code-cell'>

```python
# Custom k-point path analysis
import numpy as np

# Access band structure data directly
k_points = my_CoBS.k_distances
energies = my_CoBS.band_energies

print(f"📏 K-point path length: {len(k_points)} points")
print(f"🎵 Number of bands: {energies.shape[0]}")

# Find band gap
valence_max = np.max(energies[energies <= 0])  # Highest occupied
conduction_min = np.min(energies[energies > 0])  # Lowest unoccupied
band_gap = conduction_min - valence_max

print(f"⚡ Band gap: {band_gap:.3f} eV")
```

<div class='cell-output'>

```
📏 K-point path length: 100 points
🎵 Number of bands: 8
⚡ Band gap: 1.142 eV
```

</div>

</div>

## Visualization Tips

<div class="tip-box">
💡 <strong>Pro Tips:</strong>
<ul>
<li><strong>Interactive plots:</strong> All .html outputs are interactive - zoom, pan, and hover for details</li>
<li><strong>Custom projections:</strong> Try different orbital combinations for deeper insights</li>
<li><strong>Performance:</strong> Adjust num_kpts based on your needs (higher = more detail but slower)</li>
<li><strong>COHP interpretation:</strong> Positive values = bonding, negative = antibonding</li>
</ul>
</div>

## Related Examples

- [COHP/COOP Analysis](cohp_coop_analysis.html) - Detailed bonding analysis
- [Crystal Bonding Visualization](crystal_bonding_visualization.html) - 3D structure plots
- [COGITO Example Workflow](cogito_example.html) - Complete analysis pipeline

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

.tip-box {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 15px;
    margin: 20px 0;
}

.tip-box ul {
    margin-bottom: 0;
}

.tip-box li {
    margin-bottom: 8px;
}

.code-cell pre {
    background: transparent;
    border: none;
    margin: 0;
}

.code-cell code {
    background: transparent;
}
</style>