# COGITO Documentation Website

**Comprehensive documentation and examples for COGITO - Crystal Orbital Guided Iteration To atomic-Orbitals**

[![Website](https://img.shields.io/badge/website-live-green?style=flat-square)](https://olipemil.github.io/cogito-website)
[![COGITO](https://img.shields.io/badge/main%20repo-COGITO-blue?style=flat-square)](https://github.com/olipemil/COGITO)
[![Jekyll](https://img.shields.io/badge/built%20with-Jekyll-red?style=flat-square)](https://jekyllrb.com)

This repository hosts the documentation website for COGITO, a tool for obtaining quantum chemistry from plane wave DFT calculations. The website provides interactive tutorials, API documentation, and Jupyter notebook examples.

## Quick Start

<table>
<tr>
<td width="50%">

**Visit the live website:** [**cogito-website.github.io**](https://olipemil.github.io/cogito-website)

| Section | Description |
|---------|-------------|
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

![COGITO Workflow](docs/Si/crystal_bonds.png)
*Interactive crystal bonding visualization*

</div>

| Feature | Output | Description |
|---------|--------|-------------|
| **Chemical Bonding Analysis** | ![COHP](docs/Si/COHP_BS.png) | COHP/COOP analysis with band structure |
| **Band Structure Comparison** | ![Band Structure](docs/Si/compareDFT.png) | COGITO interpolation vs DFT validation |
| **Parameter Quality Check** | ![Decay](docs/Si/tbparams_decay.png) | Tight binding parameter decay analysis |
| **Crystal Visualization** | [Interactive Demo](https://olipemil.github.io/cogito-website) | 3D structures with actual covalent bonds |
| **Orbital Projections** | [Examples](https://olipemil.github.io/cogito-website/examples/) | Visualize atomic orbital contributions |

## Auto-Update System

The website automatically updates when the main COGITO repository changes:
- **API documentation** regenerated from source code docstrings
- **Examples** updated from latest notebooks
- **Cross-repository automation** via GitHub Actions

## Contributing

**Main COGITO Code:** Contribute to the main package at [**COGITO Repository**](https://github.com/olipemil/COGITO)

**Documentation & Website:** Improve tutorials, fix documentation issues, or enhance website functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Main Repository**: [GitHub/COGITO](https://github.com/olipemil/COGITO)
- **Issues**: [COGITO Issues](https://github.com/olipemil/COGITO/issues)
- **Website Issues**: [Website Issues](https://github.com/olipemil/cogito-website/issues)

---

<div align="center">

**[Main COGITO Repo](https://github.com/olipemil/COGITO)** |
**[Quick Start](https://olipemil.github.io/cogito-website/examples/installation_setup.html)** |
**[Examples](https://olipemil.github.io/cogito-website/examples/)**

</div>
