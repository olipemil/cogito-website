# COGITO

**Crystal Orbital Guided Iteration To atomic-Orbitals**

[![Documentation](https://img.shields.io/badge/docs-cogito--website-blue?style=flat-square)](https://olipemil.github.io/cogito-website)
[![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

COGITO is a tool for obtaining quantum chemistry from plane wave DFT calculations. The code maps the plane wave basis to atomic orbitals, enabling you to trace back which bonds contribute to independent particle energies and visualize actual quantum chemical covalent bonds in crystal structures.

## Quick Start

<table>
<tr>
<td width="50%">

**Complete documentation:** [**cogito-website.github.io**](https://olipemil.github.io/cogito-website)

| Quick Links | Description |
|-------------|-------------|
| [Installation](https://olipemil.github.io/cogito-website/examples/installation_setup.html) | Get started with COGITO setup |
| [Tutorial](https://olipemil.github.io/cogito-website/tutorial/) | Step-by-step analysis workflow |
| [Examples](https://olipemil.github.io/cogito-website/examples/) | Interactive Jupyter notebooks |
| [API Docs](https://olipemil.github.io/cogito-website/api/) | Complete function reference |

</td>
<td width="50%">

**Basic Workflow:**

1. **Run VASP** - Static calculation with saved wavefunctions
2. **Generate COGITO model** - Creates tight binding parameters
3. **Verify quality** - Check interpolation accuracy
4. **Analyze chemistry** - COHP, bonding, charge analysis

```python
from COGITOmain import COGITO

# Initialize with your VASP calculation directory
direct = "path/to/your/vasp/calculation/"
COGITOmodel = COGITO(direct)

# Generate the tight binding model
COGITOmodel.generate_TBmodel(verbose=0, plot_orbs=True)
```

</td>
</tr>
</table>

## Features & Example Results

<div align="center">

![COGITO Workflow](https://olipemil.github.io/cogito-website/docs/Si/crystal_bonds.png)
*Interactive crystal bonding visualization - [View Live Demo](https://olipemil.github.io/cogito-website)*

</div>

| Feature | Output | Description |
|---------|--------|-------------|
| **Chemical Bonding Analysis** | ![COHP](https://olipemil.github.io/cogito-website/docs/Si/COHP_BS.png) | COHP/COOP analysis with band structure |
| **Band Structure Comparison** | ![Band Structure](https://olipemil.github.io/cogito-website/docs/Si/compareDFT.png) | COGITO interpolation vs DFT validation |
| **Parameter Quality Check** | ![Decay](https://olipemil.github.io/cogito-website/docs/Si/tbparams_decay.png) | Tight binding parameter decay analysis |
| **Crystal Visualization** | [Interactive Demo](https://olipemil.github.io/cogito-website) | 3D structures with actual covalent bonds |
| **Orbital Projections** | [Examples](https://olipemil.github.io/cogito-website/examples/) | Visualize atomic orbital contributions |

## Installation

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

## Complete Analysis Example

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

## Contributing

We welcome contributions! Please see our [documentation website](https://olipemil.github.io/cogito-website) for examples and API reference.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Issues**: [GitHub Issues](https://github.com/olipemil/COGITO/issues)
- **Documentation**: [cogito-website.github.io](https://olipemil.github.io/cogito-website)
- **Examples**: [Interactive Notebooks](https://olipemil.github.io/cogito-website/examples/)

---

<div align="center">

**[Full Documentation](https://olipemil.github.io/cogito-website)** |
**[Quick Start](https://olipemil.github.io/cogito-website/examples/installation_setup.html)** |
**[Examples](https://olipemil.github.io/cogito-website/examples/)**

</div>