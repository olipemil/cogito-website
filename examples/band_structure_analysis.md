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

**Expected Output:**
```
✅ Tight binding model created successfully
```

## Generate Band Structure

```python
# Create band structure with high-symmetry path
my_CoBS = CoBS(my_CoTB, num_kpts=10)  # num_kpts per line segment

# Plot basic band structure
my_CoBS.plotBS()

print("📊 Band structure plot generated: band_structure.png")
```

**Expected Output:**
```
📊 Band structure plot generated: band_structure.png
```

## Orbital Projected Band Structure

```python
# Project onto specific orbitals
# For Silicon: s, p, d orbitals
orbital_projections = {"Si": ["s"]}  # Focus on s orbitals

my_CoBS.get_projectedBS(orbital_projections)

print("🎯 Orbital projected band structure created")
print("📁 Output: projectedBS.html (interactive plot)")
```

**Expected Output:**
```
🎯 Orbital projected band structure created
📁 Output: projectedBS.html (interactive plot)
```

## COHP Analysis

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

**Expected Output:**
```
🔬 COHP analysis completed
📁 Output: COHP_BS.html (interactive plot)
```

## Interactive COHP Dashboard

```python
# Launch interactive dashboard for COHP exploration
# This creates a web interface for dynamic COHP analysis

print("🚀 Launching interactive COHP dashboard...")
print("💡 This will open a web interface at http://127.0.0.1:8050/")

# Uncomment to run:
# my_CoBS.make_COHP_dashapp()
```

**Expected Output:**
```
🚀 Launching interactive COHP dashboard...
💡 This will open a web interface at http://127.0.0.1:8050/
```

## Advanced Analysis

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

**Expected Output:**
```
📏 K-point path length: 100 points
🎵 Number of bands: 8
⚡ Band gap: 1.142 eV
```

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
.tip-box {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 15px;
    margin: 20px 0;
}
</style>