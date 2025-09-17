---
layout: default
title: Basic Installation and Setup
parent: Examples
nav_order: 2
---

# Basic Installation and Setup

<div class="notebook-info">
    <p>📓 Getting started with COGITO installation and configuration</p>
    <p>🔗 <a href="https://github.com/olipemil/COGITO" target="_blank">COGITO Repository</a></p>
    <p>📖 <a href="../tutorial/#COGITO">Full Tutorial</a></p>
</div>

## Prerequisites

Before installing COGITO, ensure you have:
- Python 3.7 or higher
- VASP calculation outputs (INCAR, POSCAR, POTCAR, WAVECAR)
- Required Python packages (see below)

## Installation

<div class='code-cell'>

```python
# Step 1: Clone the COGITO repository
import subprocess
import sys

# Clone COGITO
subprocess.run(["git", "clone", "https://github.com/olipemil/COGITO.git"])

# Add COGITO to Python path
sys.path.insert(0, './COGITO')
```

</div>

<div class='code-cell'>

```python
# Step 2: Install required packages
packages = [
    "pymatgen",
    "matplotlib",
    "numpy",
    "scipy",
    "lmfit",
    "plotly",
    "seekpath",
    "dash"
]

for package in packages:
    subprocess.run([sys.executable, "-m", "pip", "install", package])
```

</div>

## Verify Installation

<div class='code-cell'>

```python
# Test COGITO import
try:
    from COGITO import COGITO
    print("✅ COGITO imported successfully!")

    from COGITOpost import COGITO_TB_Model as CoTB
    print("✅ COGITOpost imported successfully!")

    from COGITOpost import COGITO_BAND as CoBS
    from COGITOpost import COGITO_UNIFORM as CoUN
    print("✅ All COGITO modules imported successfully!")

except ImportError as e:
    print(f"❌ Import error: {e}")
```

<div class='cell-output'>

```
✅ COGITO imported successfully!
✅ COGITOpost imported successfully!
✅ All COGITO modules imported successfully!
```

</div>

</div>

## Basic Configuration

<div class='code-cell'>

```python
# Check your VASP calculation directory
import os

# Example directory structure
vasp_directory = "path/to/your/vasp/calculation/"

required_files = ["INCAR", "POSCAR", "POTCAR", "WAVECAR"]

print("Checking for required VASP files:")
for file in required_files:
    filepath = os.path.join(vasp_directory, file)
    if os.path.exists(filepath):
        print(f"✅ {file} found")
    else:
        print(f"❌ {file} missing")
```

</div>

## Next Steps

<div class="getting-started-note">
🎯 <strong>Ready to continue?</strong>
<br><br>
• <a href="../tutorial/">Follow the complete tutorial</a>
<br>
• <a href="cogito_example.html">Try the example workflow</a>
<br>
• <a href="../api/">Explore the API documentation</a>
</div>

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

.getting-started-note {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    border-radius: 4px;
    padding: 15px;
    margin: 20px 0;
}

.getting-started-note a {
    color: #155724;
    font-weight: 500;
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