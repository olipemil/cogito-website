# COGITOico Module

### *class* COGITOico.COGITO_ICO(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False)

Bases: `object`

#### \_\_init_\_(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False) → None

Initializes the
@param directory: The path for the input files
@param verbose: How much will be printed (0 is least)
@param file_suffix: The suffix to the TBparams and overlaps files
@param orbs_orth: Whether the orbitals are orthogonal, if from COGITO this is always False

#### read_input(file: str = 'tb_input.txt') → None

#### read_overlaps(file: str = 'overlaps.txt') → None

#### read_ICOHP(file: str = 'ICOHP.txt') → None

#### read_ICOOP(file: str = 'ICOOP.txt') → None

#### read_orbitals(file: str = 'orbitals.npy') → None

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.
@param file: Orbital file

#### save_ICOnpy()

#### *static* get_neighbors(self) → list

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

#### get_bonds_figure(energy_cutoff: float = 0.1, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.

@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
: atoms in the primitive cell. Can either be integer list to reference the default colors or
  list of plotly compatable colors. If not set defaults to elem_colors.

@param atom_labels: List of atom labels as a string.
@param plot_atom: Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

> Set between 3 (for close to orthographic) and 30 (for good perspective depth).

@return: Nothing

#### get_bonds_charge_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None, atom_dist_from_prim: float = 3.0) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.

@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
: atoms in the primitive cell. Can either be integer list to reference the default colors or
  list of plotly compatable colors. If not set defaults to elem_colors.

@param atom_labels: List of atom labels as a string.
@param auto_labels: Different options for plotting includes: (can include multiple in the string)

> “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
> “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
> “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
> “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
> NOTE: Only use “mulliken” OR “full”, NOT both

@param plot_atom: Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

> Set between 3 (for close to orthographic) and 30 (for good perspective depth).

@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.

> If False, atoms are added outside the primitive cell if the atom has a bond to an atom
> inside the primtive cell that meets energy_cutoff and bond_max criteria.
> Default is set in code False if self.numAtoms < 30, otherwise set to True

@return: Depend on return_fig parameter.

#### make_bond(atmind1, atmind2, center1, center2, orbCOOP, cartXYZ)

This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.
@param atmind1: The atom number for the first atom
@param atmind2: The atom number for the second atom
@param center1: The center of the first atom (not using self.primATOMs)
@param center2: The center of the second atom (not using self.primATOMs)
@param orbCOOP: The orbCOOP which reveals how much of each orbital combo that is included in the bond.

> Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.

@param cartXYZ: The 3D flattened grid that the bond density is calculated on
@return: A 1D array  (3D flattened) of the bond density

#### get_bond_density_figure(energy_cutoff: float = 0.1, iso_max: float = 0.03, iso_min: float = 0.003, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param iso_max: The positive isosurface for plotting the bonds.
@param iso_min: The negative isosurface for plotting the bonds.
@param elem_colors: Colors for the elements based on order in tb_input. Length of list should be the number of

> unique elements. Can either be integer list to reference the default colors or list of
> plotly compatable colors.

@param atom_colors: Colors for the atoms based on order in tb_input. Length of list should be the number of
: atoms in the primitive cell. Can either be integer list to reference the default colors or
  list of plotly compatable colors. If not set defaults to elem_colors.

@param atom_labels: List of atom labels as a string.
@param auto_label: Different options for plotting includes: (can include multiple in the string)

> “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
> “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
> “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
> “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
> NOTE: Only use “mulliken” OR “full”, NOT both

@param plot_atom: Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

> Set between 3 (for close to orthographic) and 30 (for good perspective depth).

@return: Nothing, but saves plotly figure to ‘crystal_bonds.html’

#### get_bond_info()

#### *static* get_COHP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, just_one: bool = False) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@return: returns COHP values in a [kpt,band] dimension

#### *static* get_COOP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@return: returns COHP values in a [kpt,band] dimension

#### *static* get_mulliken_charge(self: object, elem: str) → float

### COGITOico.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOico.complex128funs(phi, theta, sphharm_key)
