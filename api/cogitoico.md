---
layout: default
title: COGITOico API Reference
nav_order: 2
parent: API Documentation
---

# COGITOico API Reference

## Table of Contents

### Classes
- [COGITO_ICO](#cogito_ico)

### Functions
- [_cart_to_red](#_cart_to_red)
- [_red_to_cart](#_red_to_cart)
- [func_for_rad](#func_for_rad)
- [complex128funs](#complex128funs)

## COGITO_ICO

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L12' target='_blank'>📂 View source code</a></div>

### Methods

#### __init__

```python
__init__(self, directory, verbose, file_suffix, orbs_orth, spin_polar)
```

Initializes the
@param directory: The path for the input files
@param verbose: How much will be printed (0 is least)
@param file_suffix: The suffix to the TBparams and overlaps files
@param orbs_orth: Whether the orbitals are orthogonal, if from COGITO this is always False

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L13' target='_blank'>📍 View method source</a></div>

#### read_input

```python
read_input(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L76' target='_blank'>📍 View method source</a></div>

#### read_overlaps

```python
read_overlaps(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L158' target='_blank'>📍 View method source</a></div>

#### read_ICOHP

```python
read_ICOHP(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L249' target='_blank'>📍 View method source</a></div>

#### read_ICOOP

```python
read_ICOOP(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L373' target='_blank'>📍 View method source</a></div>

#### read_orbitals

```python
read_orbitals(self, file)
```

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in 'orbitals.npy' is combined with the orbital data in 'tb_input.txt'.
@param file: Orbital file

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L449' target='_blank'>📍 View method source</a></div>

#### save_ICOnpy

```python
save_ICOnpy(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L490' target='_blank'>📍 View method source</a></div>

#### get_neighbors

```python
get_neighbors(self)
```

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L496' target='_blank'>📍 View method source</a></div>

#### get_bonds_figure

```python
get_bonds_figure(self, energy_cutoff, elem_colors, atom_colors, atom_labels, plot_atom, one_atom, bond_max, fovy, return_fig)
```

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of
                    unique elements. Can either be integer list to reference the default colors or list of
                    plotly compatable colors.
@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
                    atoms in the primitive cell. Can either be integer list to reference the default colors or
                    list of plotly compatable colors. If not set defaults to elem_colors.
@param atom_labels: List of atom labels as a string.
@param plot_atom: Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
                Set between 3 (for close to orthographic) and 30 (for good perspective depth).
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L514' target='_blank'>📍 View method source</a></div>

#### get_bonds_charge_figure

```python
get_bonds_charge_figure(self, energy_cutoff, bond_max, elem_colors, atom_colors, atom_labels, auto_label, plot_atom, one_atom, fovy, return_fig, only_prim_atoms, atom_dist_from_prim)
```

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of
                    unique elements. Can either be integer list to reference the default colors or list of
                    plotly compatable colors.
@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
                    atoms in the primitive cell. Can either be integer list to reference the default colors or
                    list of plotly compatable colors. If not set defaults to elem_colors.
@param atom_labels: List of atom labels as a string.
@param auto_labels: Different options for plotting includes: (can include multiple in the string)
                    "mulliken" - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
                    "full" - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
                    "color" - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
                    "color mag" - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
                    NOTE: Only use "mulliken" OR "full", NOT both
@param plot_atom: Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
                Set between 3 (for close to orthographic) and 30 (for good perspective depth).
@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.
                        If False, atoms are added outside the primitive cell if the atom has a bond to an atom
                        inside the primtive cell that meets energy_cutoff and bond_max criteria.
                        Default is set in code False if self.numAtoms < 30, otherwise set to True
@return: Depend on return_fig parameter.

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L1188' target='_blank'>📍 View method source</a></div>

#### make_bond

```python
make_bond(self, atmind1, atmind2, center1, center2, orbCOOP, cartXYZ)
```

This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.
@param atmind1: The atom number for the first atom
@param atmind2: The atom number for the second atom
@param center1: The center of the first atom (not using self.primATOMs)
@param center2: The center of the second atom (not using self.primATOMs)
@param orbCOOP: The orbCOOP which reveals how much of each orbital combo that is included in the bond.
                Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.
@param cartXYZ: The 3D flattened grid that the bond density is calculated on
@return: A 1D array  (3D flattened) of the bond density

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L2279' target='_blank'>📍 View method source</a></div>

#### get_bond_density_figure

```python
get_bond_density_figure(self, energy_cutoff, iso_max, iso_min, elem_colors, atom_colors, atom_labels, auto_label, plot_atom, one_atom, bond_max, fovy, return_fig)
```

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param iso_max: The positive isosurface for plotting the bonds.
@param iso_min: The negative isosurface for plotting the bonds.
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of
                    unique elements. Can either be integer list to reference the default colors or list of
                    plotly compatable colors.
@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
                    atoms in the primitive cell. Can either be integer list to reference the default colors or
                    list of plotly compatable colors. If not set defaults to elem_colors.
@param atom_labels: List of atom labels as a string.
@param auto_label: Different options for plotting includes: (can include multiple in the string)
                    "mulliken" - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
                    "full" - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
                    "color" - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
                    "color mag" - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
                    NOTE: Only use "mulliken" OR "full", NOT both
@param plot_atom: Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
                Set between 3 (for close to orthographic) and 30 (for good perspective depth).
@return: Nothing, but saves plotly figure to 'crystal_bonds.html'

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L2357' target='_blank'>📍 View method source</a></div>

#### get_bond_info

```python
get_bond_info(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3482' target='_blank'>📍 View method source</a></div>

#### get_COHP

```python
get_COHP(self, orbs, NN, include_onsite, just_one)
```

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@return: returns COHP values in a [kpt,band] dimension

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3703' target='_blank'>📍 View method source</a></div>

#### get_COOP

```python
get_COOP(self, orbs, NN, include_onsite, spin)
```

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@return: returns COHP values in a [kpt,band] dimension

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3801' target='_blank'>📍 View method source</a></div>

#### get_mulliken_charge

```python
get_mulliken_charge(self, elem)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3900' target='_blank'>📍 View method source</a></div>

## _cart_to_red

```python
_cart_to_red(tmp, cart)
```

Convert cartesian vectors cart to reduced coordinates of a1,a2,a3 vectors

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3947' target='_blank'>📂 View source code</a></div>

## _red_to_cart

```python
_red_to_cart(prim_vec, prim_coord)
```

:param prim_vec: three float tuples representing the primitive vectors
:param prim_coord: list of float tuples for primitive coordinates
:return: list of float tuples for cartesian coordinates
        ex: cart_coord = _red_to_cart((a1,a2,a3),prim_coord)

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3963' target='_blank'>📂 View source code</a></div>

## func_for_rad

```python
func_for_rad(x, a, b, c, d, e, f, g, h, l)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3978' target='_blank'>📂 View source code</a></div>

## complex128funs

```python
complex128funs(phi, theta, sphharm_key)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3981' target='_blank'>📂 View source code</a></div>

