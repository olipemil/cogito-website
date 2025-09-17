---
layout: default
title: COGITOpost API Reference
nav_order: 2
parent: API Documentation
---

# COGITOpost API Reference

## Table of Contents

### Classes
- [COGITO_TB_Model](#cogito_tb_model)
- [COGITO_BAND](#cogito_band)
- [COGITO_UNIFORM](#cogito_uniform)
- [COGITO_BS_widget](#cogito_bs_widget)

### Functions
- [_cart_to_red](#_cart_to_red)
- [_red_to_cart](#_red_to_cart)
- [func_for_rad](#func_for_rad)
- [complex128funs](#complex128funs)

## COGITO_TB_Model

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L12' target='_blank'>📂 View source code</a></div>

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

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L13' target='_blank'>📍 View method source</a></div>

#### read_input

```python
read_input(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L55' target='_blank'>📍 View method source</a></div>

#### read_TBparams

```python
read_TBparams(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L138' target='_blank'>📍 View method source</a></div>

#### read_overlaps

```python
read_overlaps(self, file)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L222' target='_blank'>📍 View method source</a></div>

#### read_orbitals

```python
read_orbitals(self, file)
```

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in 'orbitals.npy' is combined with the orbital data in 'tb_input.txt'.
@param file: Orbital file

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L285' target='_blank'>📍 View method source</a></div>

#### normalize_params

```python
normalize_params(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L329' target='_blank'>📍 View method source</a></div>

#### set_hoppings

```python
set_hoppings(self, value, orb1, orb2, trans, spin)
```

Change a TB parameter
@param value: The new parameter
@param orb1: The first orbital index of the parameter
@param orb2: The second orbital index of the parameter
@param trans: The tuple of translation indices
@return:

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L359' target='_blank'>📍 View method source</a></div>

#### restrict_params

```python
restrict_params(self, maximum_dist, minimum_value)
```

Generates self.use_tbparams, self.use_overlaps, and self.use_vecs_to_orbs which are used in the gen_ham() funciton
With this, the calculation of hamiltonians by gen_ham() is both sparse and vectorized
@param maximum_dist: The maximmum distance between hopping parameters which should be included
@param minimum_value: The minimum magnitude of hopping parameter which should be included

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L371' target='_blank'>📍 View method source</a></div>

#### make_orbitals

```python
make_orbitals(self, cartXYZ)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L431' target='_blank'>📍 View method source</a></div>

#### plot_orbitals

```python
plot_orbitals(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L484' target='_blank'>📍 View method source</a></div>

#### generate_gpnts

```python
generate_gpnts(self, kpt)
```

similar to from pymatgen.io.vasp.outputs.Wavecar but is vectorized
@param kpt: The k-point in reduced coordinates
@return: The gpoints

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L596' target='_blank'>📍 View method source</a></div>

#### get_ham

```python
get_ham(self, kpt, return_overlap, return_truevec, spin)
```

This function generates the hamiltonian and overlap matrices for a given kpt.
Then it solves the generalized eigenvalue problem to return the eigvalues and vectors
@param self: An object with the attributes of the COGITO_TB_Model class
@param kpt: The kpoint to regenerate at in reduced coordinates
@param return_overlap: If True, the function will also return the overlap matrix at the kpt; default is False
@param return_truevec: If True, the function will return the eigenvectors in the original nonorthogonal basis
                        Default if True
@param spin: The spin of the parameters for a spin-polarized calculation; default is 0--for non spin-polarized
@return: returns a list of the eigenvalues and eigenvectors (and overlap if return_overlap=True)

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L628' target='_blank'>📍 View method source</a></div>

#### get_fullHam

```python
get_fullHam(self, kpt, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L688' target='_blank'>📍 View method source</a></div>

#### get_neighbors

```python
get_neighbors(self)
```

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L698' target='_blank'>📍 View method source</a></div>

#### plot_crystal_field

```python
plot_crystal_field(self, atomnum, orbitals, ylim, spin)
```

Plots the crystal field splitting diagram for the orbitals and atom given
@param atomnum: Which atom to plot for
@param orbitals: Which orbitals to plot, "d" is most common
@param ylim: The limits of the y-axis in the plot, will default to good value if left (-10,0)

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L717' target='_blank'>📍 View method source</a></div>

#### plot_hopping

```python
plot_hopping(self, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L804' target='_blank'>📍 View method source</a></div>

#### plot_overlaps

```python
plot_overlaps(self, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L845' target='_blank'>📍 View method source</a></div>

#### compare_to_DFT

```python
compare_to_DFT(self, directory, extra_tag)
```

This function reads the EIGENVAL from a DFT run, generates the energies from the TB model for the kpt grid,
And plots and compares the error between the TB model energies and DFT energies
@param self: An object of the class COGITO_TB_Model (can not be the BAND or UNIFORM classes!)
@param directory: The directory where the EIGENVAL file is
@return: Returns a list of the (averaged over the valance bands) band distance (as defined by Marzari),
        average maximum error, and average band error

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L884' target='_blank'>📍 View method source</a></div>

#### get_COHP

```python
get_COHP(self, orbs, NN, include_onsite, spin)
```

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@param spin: The spin of the tight binding parameters; default is 0 works for nonspin-polarized
@return: returns COHP values in a [kpt,band] dimension

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1007' target='_blank'>📍 View method source</a></div>

#### get_ICOHP

```python
get_ICOHP(self, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1136' target='_blank'>📍 View method source</a></div>

#### get_COOP

```python
get_COOP(self, orbs, NN, include_onsite, spin)
```

Calculates the COOP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param include_onsite: Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
@param spin: The spin of the tight binding parameters; default is 0 works for nonspin-polarized
@return: returns COOP values in a [kpt,band] dimension

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1170' target='_blank'>📍 View method source</a></div>

#### get_ICOOP

```python
get_ICOOP(self, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1293' target='_blank'>📍 View method source</a></div>

## COGITO_BAND

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1326' target='_blank'>📂 View source code</a></div>

### Methods

#### __init__

```python
__init__(self, TB_model, num_kpts)
```

This class deals with all post-processing band structure analysis
@param TB_model: requires an object of the class COGITO_TB_Model

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1327' target='_blank'>📍 View method source</a></div>

#### get_bandstructure

```python
get_bandstructure(self, num_kpts)
```

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath
@param num_kpts: The number of kpoints between EACH kpath
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1343' target='_blank'>📍 View method source</a></div>

#### plotBS

```python
plotBS(self, ax, ylim, color_label, colors, colorhalf)
```

@param ax (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
@param ylim: Limits on the y-axis of plot
@param color_label: When being plotted from another function, this passes "COHP" or "COOP"
@param colors: Magnitude for each point to use in color plotting, passed by get_COHP() function
@param colorhalf: Sets scale of color bar
@return: matplotlib.pyplot axis with bandstructure plotted

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1385' target='_blank'>📍 View method source</a></div>

#### plotlyBS

```python
plotlyBS(self, ylim, color_label, colors, colorhalf, orbProj)
```

Plots bandstructure (or projected bandstructure) using plotly graph_objects
@param ylim: Limits on the y-axis of plot
@param color_label: When being plotted from another function, this passes "COHP" or "COOP"
@param colors: Magnitude for each point to use in color plotting, passed by get_COHP() function
@param colorhalf: Sets scale of color bar
@return: plotly figure with bandstructure plotted

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1467' target='_blank'>📍 View method source</a></div>

#### get_COHP

```python
get_COHP(self, orbs, NN, ylim, colorhalf, include_onsite, from_dash)
```

Calculates and plots the projected COHP values for each band and k-point on band structure
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param ylim: The limits of the y-axis (energy) of the band structure plot
@param colorhalf: Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COHP)*3
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@param from_dash: Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1567' target='_blank'>📍 View method source</a></div>

#### get_COOP

```python
get_COOP(self, orbs, NN, ylim, colorhalf, include_onsite, from_dash, color_label, orbProj)
```

Calculates and plots the projected COOP values for each band and k-point on band structure
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors
@param ylim: The limits of the y-axis (energy) of the band structure plot
@param colorhalf: Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COOP)*3
@param include_onsite: Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
@param from_dash: Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1592' target='_blank'>📍 View method source</a></div>

#### get_projectedBS

```python
get_projectedBS(self, orbdict, ylim, colorhalf)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1616' target='_blank'>📍 View method source</a></div>

#### make_COHP_dashapp

```python
make_COHP_dashapp(self, pathname)
```

This function generate a dash app which allows the user to interactively select orbitals and nearest neighbors
to examine their project COHP band structure quickly
@param pathname: Name appended to the default pathname for the html
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1629' target='_blank'>📍 View method source</a></div>

## COGITO_UNIFORM

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1727' target='_blank'>📂 View source code</a></div>

### Methods

#### __init__

```python
__init__(self, TB_model, grid)
```

This class deals with all post-processing uniform grid analysis
@param TB_model: requires an object of the class COGITO_TB_Model

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1728' target='_blank'>📍 View method source</a></div>

#### get_uniform

```python
get_uniform(self, grid)
```

@param grid: The kpoint grid to use for the uniform sampling

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1744' target='_blank'>📍 View method source</a></div>

#### recalc_efermi

```python
recalc_efermi(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1810' target='_blank'>📍 View method source</a></div>

#### get_occupation

```python
get_occupation(self, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1814' target='_blank'>📍 View method source</a></div>

#### get_COHP

```python
get_COHP(self, orbs, NN, ylim, sigma, include_onsite)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1889' target='_blank'>📍 View method source</a></div>

#### get_ICOHP

```python
get_ICOHP(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1960' target='_blank'>📍 View method source</a></div>

#### save_ICOHP

```python
save_ICOHP(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L1997' target='_blank'>📍 View method source</a></div>

#### get_COOP

```python
get_COOP(self, orbs, NN, ylim, sigma, include_onsite, orbProj, label)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2033' target='_blank'>📍 View method source</a></div>

#### get_projectedDOS

```python
get_projectedDOS(self, elem, ylim, sigma, colorhalf)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2115' target='_blank'>📍 View method source</a></div>

#### get_ICOOP

```python
get_ICOOP(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2226' target='_blank'>📍 View method source</a></div>

#### save_ICOOP

```python
save_ICOOP(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2266' target='_blank'>📍 View method source</a></div>

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

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2302' target='_blank'>📍 View method source</a></div>

#### get_bonds_figure_old

```python
get_bonds_figure_old(self, energy_cutoff, offset, plot_atom, one_atom, bond_max)
```

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param offset: The offset in the colors, set different values to try out different colors
@param plot_atom: Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2384' target='_blank'>📍 View method source</a></div>

#### get_bonds_figure

```python
get_bonds_figure(self, energy_cutoff, bond_max, elem_colors, atom_colors, atom_labels, plot_atom, one_atom, fovy, return_fig, only_prim_atoms)
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
@param plot_atom: Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
                Set between 3 (for close to orthographic) and 30 (for good perspective depth).
@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.
                        If False, atoms are added outside the primitive cell if the atom has a bond to an atom
                        inside the primtive cell that meets energy_cutoff and bond_max criteria.
                        Default is set in code False if self.numAtoms < 30, otherwise set to True
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L2769' target='_blank'>📍 View method source</a></div>

#### get_bonds_charge_figure

```python
get_bonds_charge_figure(self, energy_cutoff, bond_max, elem_colors, atom_colors, atom_labels, auto_label, plot_atom, one_atom, fovy, return_fig, only_prim_atoms)
```

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
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
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
                Set between 3 (for close to orthographic) and 30 (for good perspective depth).
@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.
                        If False, atoms are added outside the primitive cell if the atom has a bond to an atom
                        inside the primtive cell that meets energy_cutoff and bond_max criteria.
                        Default is set in code False if self.numAtoms < 30, otherwise set to True
@return: Depend on return_fig parameter.

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L3446' target='_blank'>📍 View method source</a></div>

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

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L4516' target='_blank'>📍 View method source</a></div>

#### get_bond_info

```python
get_bond_info(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L5642' target='_blank'>📍 View method source</a></div>

#### get_COHP_DOS_bybond

```python
get_COHP_DOS_bybond(self, sigma, return_fig)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L5862' target='_blank'>📍 View method source</a></div>

#### get_crystal_plus_COHP

```python
get_crystal_plus_COHP(self, energy_cutoff, bond_max, auto_label, fovy)
```

The will plot the crystal bond plot on the left with interactivity to a COHP DOS plot on the right
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param auto_label: Different options for plotting includes: (can include multiple in the string)
                    "mulliken" - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
                    "full" - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
                    "color" - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
                    "color mag" - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
                    NOTE: Only use "mulliken" OR "full", NOT both
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
@return: Nothing, but saved to 'bond_cohp_plot.html'

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6298' target='_blank'>📍 View method source</a></div>

#### get_mulliken_charge

```python
get_mulliken_charge(self, elem)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6755' target='_blank'>📍 View method source</a></div>

## COGITO_BS_widget

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6802' target='_blank'>📂 View source code</a></div>

### Methods

#### __init__

```python
__init__(self, TB_model, num_kpts)
```

This class deals with all post-processing band structure analysis
@param TB_model: requires an object of the class COGITO_TB_Model

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6803' target='_blank'>📍 View method source</a></div>

#### get_bandstructure

```python
get_bandstructure(self, num_kpts)
```

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath
@param num_kpts: The number of kpoints between EACH kpath
@return: Nothing

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6819' target='_blank'>📍 View method source</a></div>

#### plotlyBS

```python
plotlyBS(self, ylim, selectedDot, plotnew)
```

Plots bandstructure (or projected bandstructure) using plotly graph_objects
@param ylim: Limits on the y-axis of plot
@return: plotly figure with bandstructure plotted

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6863' target='_blank'>📍 View method source</a></div>

#### plotBS

```python
plotBS(self, ax, selectedDot, plotnew, ylim)
```

:param ax (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
:param selectedDot (1D integer array): gives kpoint and band index of the dot selected to make green circle
                        eg: [3,4]
:return: matplotlib.pyplot axis with bandstructure plotted

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L6949' target='_blank'>📍 View method source</a></div>

#### get_significant_bonds

```python
get_significant_bonds(self, band, kpoint, spin)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7017' target='_blank'>📍 View method source</a></div>

#### plot_bond_run

```python
plot_bond_run(self, num_bond)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7171' target='_blank'>📍 View method source</a></div>

#### change_sig_bonds

```python
change_sig_bonds(self, old_vals, new_vals, tbvals, num_bond)
```

To change tight-binding parameter, need to know two orbitals and three translations

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7268' target='_blank'>📍 View method source</a></div>

#### make_BS_widget

```python
make_BS_widget(self, app)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7297' target='_blank'>📍 View method source</a></div>

## _cart_to_red

```python
_cart_to_red(tmp, cart)
```

Convert cartesian vectors cart to reduced coordinates of a1,a2,a3 vectors

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7538' target='_blank'>📂 View source code</a></div>

## _red_to_cart

```python
_red_to_cart(prim_vec, prim_coord)
```

:param prim_vec: three float tuples representing the primitive vectors
:param prim_coord: list of float tuples for primitive coordinates
:return: list of float tuples for cartesian coordinates
        ex: cart_coord = _red_to_cart((a1,a2,a3),prim_coord)

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7554' target='_blank'>📂 View source code</a></div>

## func_for_rad

```python
func_for_rad(x, a, b, c, d, e, f, g, h, l)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7569' target='_blank'>📂 View source code</a></div>

## complex128funs

```python
complex128funs(phi, theta, sphharm_key)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITOpost.py#L7572' target='_blank'>📂 View source code</a></div>

