# COGITO

**Crystal Orbital Guided Iteration To atomic-Orbitals**

[![Documentation](https://img.shields.io/badge/docs-cogito--website-blue?style=flat-square)](https://olipemil.github.io/cogito-website)
[![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

COGITO is a tool for obtaining quantum chemistry from plane wave DFT calculations. The code maps the plane wave basis to atomic orbitals, enabling you to trace back which bonds contribute to independent particle energies and visualize actual quantum chemical covalent bonds in crystal structures.

## 🚀 Quick Start

```python
from COGITOmain import COGITO

# Initialize with your VASP calculation directory
direct = "path/to/your/vasp/calculation/"
COGITOmodel = COGITO(direct)

# Generate the tight binding model
COGITOmodel.generate_TBmodel(verbose=0, plot_orbs=True)
```

## 📖 Documentation & Examples

**Complete documentation and interactive examples:** [**cogito-website.github.io**](https://olipemil.github.io/cogito-website)

| Quick Links | Description |
|-------------|-------------|
| [🔧 Installation](https://olipemil.github.io/cogito-website/examples/installation_setup.html) | Get started with COGITO setup |
| [📚 Tutorial](https://olipemil.github.io/cogito-website/tutorial/) | Step-by-step analysis workflow |
| [💻 Examples](https://olipemil.github.io/cogito-website/examples/) | Interactive Jupyter notebooks |
| [📑 API Docs](https://olipemil.github.io/cogito-website/api/) | Complete function reference |

## ✨ Key Features

<div align="center">

![COGITO Workflow](https://olipemil.github.io/cogito-website/docs/Si/crystal_bonds.png)
*Interactive crystal bonding visualization - [View Live Demo](https://olipemil.github.io/cogito-website)*

</div>

- **🔬 Chemical Bonding Analysis** - COHP/COOP analysis with band structure
- **📊 Band Structure** - Compare COGITO interpolation with DFT
- **⚛️ Orbital Projections** - Visualize atomic orbital contributions
- **🏗️ Crystal Visualization** - 3D structures with actual covalent bonds
- **📈 Quality Verification** - Built-in validation against VASP calculations

## 🔧 Installation

### Requirements
- Python 3.7+
- VASP calculation outputs (POSCAR, POTCAR, WAVECAR, OUTCAR, vasprun.xml)

### Dependencies
```bash
pip install pymatgen matplotlib numpy scipy lmfit plotly seekpath
```

### Install COGITO
```bash
git clone https://github.com/olipemil/COGITO.git
export PYTHONPATH="${PYTHONPATH}:/path/to/COGITO"
```

## 🎯 Basic Workflow

1. **Run VASP** - Static calculation with saved wavefunctions
2. **Generate COGITO model** - Creates tight binding parameters
3. **Verify quality** - Check interpolation accuracy
4. **Analyze chemistry** - COHP, bonding, charge analysis

```python
# Step 1: Generate COGITO model
from COGITOmain import COGITO
COGITOmodel = COGITO("your_vasp_directory/")
COGITOmodel.generate_TBmodel()

# Step 2: Analyze results
from COGITOpost import COGITO_analyze as coze
COGITOTB = coze("your_vasp_directory/")
COGITOTB.compare_to_DFT("your_vasp_directory/")
COGITOTB.get_bandstructure()
```

## 📊 Example Results

| Analysis Type | Output | Description |
|---------------|--------|-------------|
| **Band Structure** | ![Band Structure](https://olipemil.github.io/cogito-website/docs/Si/compareDFT.png) | COGITO vs DFT comparison |
| **COHP Analysis** | ![COHP](https://olipemil.github.io/cogito-website/docs/Si/COHP_BS.png) | Bonding/antibonding contributions |
| **Parameter Decay** | ![Decay](https://olipemil.github.io/cogito-website/docs/Si/tbparams_decay.png) | Tight binding quality check |

## 🤝 Contributing

We welcome contributions! Please see our [documentation website](https://olipemil.github.io/cogito-website) for examples and API reference.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📮 Contact

- **Issues**: [GitHub Issues](https://github.com/olipemil/COGITO/issues)
- **Documentation**: [cogito-website.github.io](https://olipemil.github.io/cogito-website)
- **Examples**: [Interactive Notebooks](https://olipemil.github.io/cogito-website/examples/)

---

<div align="center">

**[📖 Full Documentation](https://olipemil.github.io/cogito-website)** |
**[🚀 Quick Start](https://olipemil.github.io/cogito-website/examples/installation_setup.html)** |
**[💻 Examples](https://olipemil.github.io/cogito-website/examples/)**

</div>