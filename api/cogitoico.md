---
layout: default
title: COGITOico API Reference
nav_order: 4
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

# COGITOico Module

### *class* COGITOico.COGITO_ICO(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False)

Bases: `object`

#### \_\_init_\_(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False) → None

Initializes the
:param directory: The path for the input files
:param verbose: How much will be printed (0 is least)
:param file_suffix: The suffix to the TBparams and overlaps files
:param orbs_orth: Whether the orbitals are orthogonal, if from COGITO this is always False

#### read_input(file: str = 'tb_input.txt') → None

#### read_overlaps(file: str = 'overlaps.txt') → None

#### read_ICOHP(file: str = 'ICOHP.txt') → None

#### read_ICOOP(file: str = 'ICOOP.txt') → None

#### read_orbitals(file: str = 'orbitals.npy') → None

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.
:param file: Orbital file

#### save_ICOnpy()

#### *static* get_neighbors(self) → list

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

#### get_bonds_figure(energy_cutoff: float = 0.1, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
:param energy_cutoff: This is the minimum bond magnitude that will be plotted
:param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.
* **Parameters:**
  * **atom_colors** – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** – List of atom labels as a string.
  * **plot_atom** – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** – Whether only the atom defined in plot_atom should be plotted; default is False
  * **bond_max** – The maximum bond distance that will be plotted outside the primitive cell
  * **fovy** – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
* **Returns:**
  Nothing

#### get_bonds_charge_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None, atom_dist_from_prim: float = 3.0) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
:param energy_cutoff: This is the minimum bond magnitude that will be plotted
:param bond_max: The maximum bond distance that will be plotted outside the primitive cell
:param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.
* **Parameters:**
  * **atom_colors** – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** – List of atom labels as a string.
  * **auto_labels** – Different options for plotting includes: (can include multiple in the string)
    “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
    “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
    “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
    “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
    NOTE: Only use “mulliken” OR “full”, NOT both
  * **plot_atom** – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** – Whether only the atom defined in plot_atom should be plotted; default is False
  * **fovy** – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
  * **return_fig** – If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
  * **only_prim_atoms** – If True, only the atoms within the primitive cell are plotted.
    If False, atoms are added outside the primitive cell if the atom has a bond to an atom
    inside the primtive cell that meets energy_cutoff and bond_max criteria.
    Default is set in code False if self.numAtoms < 30, otherwise set to True
* **Returns:**
  Depend on return_fig parameter.

#### make_bond(atmind1, atmind2, center1, center2, orbCOOP, cartXYZ)

This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.
:param atmind1: The atom number for the first atom
:param atmind2: The atom number for the second atom
:param center1: The center of the first atom (not using self.primATOMs)
:param center2: The center of the second atom (not using self.primATOMs)
:param orbCOOP: The orbCOOP which reveals how much of each orbital combo that is included in the bond.

> Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.
* **Parameters:**
  **cartXYZ** – The 3D flattened grid that the bond density is calculated on
* **Returns:**
  A 1D array  (3D flattened) of the bond density

#### get_bond_density_figure(energy_cutoff: float = 0.1, iso_max: float = 0.03, iso_min: float = 0.003, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label
:param energy_cutoff: This is the minimum bond magnitude that will be plotted
:param iso_max: The positive isosurface for plotting the bonds.
:param iso_min: The negative isosurface for plotting the bonds.
:param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.
* **Parameters:**
  * **atom_colors** – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** – List of atom labels as a string.
  * **auto_label** – Different options for plotting includes: (can include multiple in the string)
    “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
    “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
    “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
    “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
    NOTE: Only use “mulliken” OR “full”, NOT both
  * **plot_atom** – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** – Whether only the atom defined in plot_atom should be plotted; default is False
  * **bond_max** – The maximum bond distance that will be plotted outside the primitive cell
  * **fovy** – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
* **Returns:**
  Nothing, but saves plotly figure to ‘crystal_bonds.html’

#### get_bond_info()

#### *static* get_COHP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, just_one: bool = False) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors
:param self: An object of the class COGITO_BAND or COGITO_UNIFORM
:param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
:param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
:param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
:returns: returns COHP values in a [kpt,band] dimension

#### *static* get_COOP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors
:param self: An object of the class COGITO_BAND or COGITO_UNIFORM
:param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
:param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
:param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
:returns: returns COHP values in a [kpt,band] dimension

#### *static* get_mulliken_charge(self: object, elem: str) → float

### COGITOico.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOico.complex128funs(phi, theta, sphharm_key)
