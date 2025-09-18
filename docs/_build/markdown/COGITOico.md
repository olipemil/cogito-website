# COGITOico module

### *class* COGITOico.COGITO_ICO(directory, verbose=0, file_suffix='', orbs_orth=False, spin_polar=False)

Bases: `object`

* **Parameters:**
  * **directory** (*str*)
  * **verbose** (*int*)
  * **file_suffix** (*str*)
  * **orbs_orth** (*bool*)
  * **spin_polar** (*bool*)

#### \_\_init_\_(directory, verbose=0, file_suffix='', orbs_orth=False, spin_polar=False)

Initializes the

**Parameters:**
: directory (str): The path for the input files
  verbose (int): How much will be printed (0 is least)
  file_suffix (str): The suffix to the TBparams and overlaps files
  orbs_orth (bool): Whether the orbitals are orthogonal, if from COGITO this is always False

* **Parameters:**
  * **directory** (*str*)
  * **verbose** (*int*)
  * **file_suffix** (*str*)
  * **orbs_orth** (*bool*)
  * **spin_polar** (*bool*)
* **Return type:**
  None

#### read_input(file='tb_input.txt')

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### read_overlaps(file='overlaps.txt')

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### read_ICOHP(file='ICOHP.txt')

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### read_ICOOP(file='ICOOP.txt')

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### read_orbitals(file='orbitals.npy')

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.

**Parameters:**
: file (str): Orbital file

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### save_ICOnpy()

#### *static* get_neighbors(self)

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

* **Return type:**
  list

#### get_bonds_figure(energy_cutoff=0.1, elem_colors=[], atom_colors=[], atom_labels=[], plot_atom=None, one_atom=False, bond_max=3.0, fovy=10, return_fig=False)

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

**Parameters:**
: energy_cutoff (float): This is the minimum bond magnitude that will be plotted
  elem_colors (list): Colors for the elements based on order in tb_input. Length of list should be the number of
  <br/>
  > unique elements. Can either be integer list to reference the default colors or list of
  > plotly compatable colors.
  <br/>
  atom_colors (list): Colors for the atoms based on order in tb_input. Length of list should be the number of
  : atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  <br/>
  atom_labels (list): List of atom labels as a string.
  plot_atom (int): Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  one_atom (bool): Whether only the atom defined in plot_atom should be plotted; default is False
  bond_max (float): The maximum bond distance that will be plotted outside the primitive cell
  fovy (float): field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
  <br/>
  > Set between 3 (for close to orthographic) and 30 (for good perspective depth).

**Returns:**
: None: Nothing

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **elem_colors** (*list*)
  * **atom_colors** (*list*)
  * **atom_labels** (*list*)
  * **plot_atom** (*int* *|* *None*)
  * **one_atom** (*bool*)
  * **bond_max** (*float*)
  * **fovy** (*float*)
  * **return_fig** (*bool*)
* **Return type:**
  None

#### get_bonds_charge_figure(energy_cutoff=0.1, bond_max=3.0, elem_colors=[], atom_colors=[], atom_labels=[], auto_label='', plot_atom=None, one_atom=False, fovy=10, return_fig=False, only_prim_atoms=None, atom_dist_from_prim=3.0)

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

> “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
> “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
> “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
> “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
> NOTE: Only use “mulliken” OR “full”, NOT both

**Parameters:**
: energy_cutoff (float): This is the minimum bond magnitude that will be plotted
  bond_max (float): The maximum bond distance that will be plotted outside the primitive cell
  elem_colors (list): Colors for the elements based on order in tb_input. Length of list should be the number of
  <br/>
  > unique elements. Can either be integer list to reference the default colors or list of
  > plotly compatable colors.
  <br/>
  atom_colors (list): Colors for the atoms based on order in tb_input. Length of list should be the number of
  : atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  <br/>
  atom_labels (list): List of atom labels as a string.
  plot_atom (int): Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  one_atom (bool): Whether only the atom defined in plot_atom should be plotted; default is False
  fovy (float): field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
  <br/>
  > Set between 3 (for close to orthographic) and 30 (for good perspective depth).
  <br/>
  return_fig (bool): If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
  only_prim_atoms (bool): If True, only the atoms within the primitive cell are plotted.
  <br/>
  > If False, atoms are added outside the primitive cell if the atom has a bond to an atom
  > inside the primtive cell that meets energy_cutoff and bond_max criteria.
  > Default is set in code False if self.numAtoms < 30, otherwise set to True

**Returns:**
: None: Depend on return_fig parameter.

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **bond_max** (*float*)
  * **elem_colors** (*list*)
  * **atom_colors** (*list*)
  * **atom_labels** (*list*)
  * **auto_label** (*str*)
  * **plot_atom** (*int* *|* *None*)
  * **one_atom** (*bool*)
  * **fovy** (*float*)
  * **return_fig** (*bool*)
  * **only_prim_atoms** (*bool* *|* *None*)
  * **atom_dist_from_prim** (*float*)
* **Return type:**
  None

#### make_bond(atmind1, atmind2, center1, center2, orbCOOP, cartXYZ)

This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.

**Parameters:**
: atmind1 (unknown): The atom number for the first atom
  atmind2 (unknown): The atom number for the second atom
  center1 (unknown): The center of the first atom (not using self.primATOMs)
  center2 (unknown): The center of the second atom (not using self.primATOMs)
  orbCOOP (unknown): The orbCOOP which reveals how much of each orbital combo that is included in the bond.
  <br/>
  > Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.
  <br/>
  cartXYZ (unknown): The 3D flattened grid that the bond density is calculated on

**Returns:**
: unknown: A 1D array  (3D flattened) of the bond density

#### get_bond_density_figure(energy_cutoff=0.1, iso_max=0.03, iso_min=0.003, elem_colors=[], atom_colors=[], atom_labels=[], auto_label='', plot_atom=None, one_atom=False, bond_max=3.0, fovy=10, return_fig=False)

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label

**Parameters:**
: energy_cutoff (float): This is the minimum bond magnitude that will be plotted
  iso_max (float): The positive isosurface for plotting the bonds.
  iso_min (float): The negative isosurface for plotting the bonds.
  elem_colors (list): Colors for the elements based on order in tb_input. Length of list should be the number of
  <br/>
  > unique elements. Can either be integer list to reference the default colors or list of
  > plotly compatable colors.
  <br/>
  atom_colors (list): Colors for the atoms based on order in tb_input. Length of list should be the number of
  : atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  <br/>
  atom_labels (list): List of atom labels as a string.
  auto_label (str): Different options for plotting includes: (can include multiple in the string)
  <br/>
  > “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
  > “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
  > “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
  > “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
  > NOTE: Only use “mulliken” OR “full”, NOT both
  <br/>
  plot_atom (int): Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  one_atom (bool): Whether only the atom defined in plot_atom should be plotted; default is False
  bond_max (float): The maximum bond distance that will be plotted outside the primitive cell
  fovy (float): field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
  <br/>
  > Set between 3 (for close to orthographic) and 30 (for good perspective depth).

**Returns:**
: None: Nothing, but saves plotly figure to ‘crystal_bonds.html’

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **iso_max** (*float*)
  * **iso_min** (*float*)
  * **elem_colors** (*list*)
  * **atom_colors** (*list*)
  * **atom_labels** (*list*)
  * **auto_label** (*str*)
  * **plot_atom** (*int* *|* *None*)
  * **one_atom** (*bool*)
  * **bond_max** (*float*)
  * **fovy** (*float*)
  * **return_fig** (*bool*)
* **Return type:**
  None

#### get_bond_info()

#### *static* get_COHP(self, orbs, NN=None, include_onsite=False, just_one=False)

Calculates the COHP for the given orbitals and nearest neighbors

**Parameters:**
: self (object): An object of the class COGITO_BAND or COGITO_UNIFORM
  orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  include_onsite (bool): Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms

**Returns:**
: npt.NDArray: returns COHP values in a [kpt,band] dimension

* **Parameters:**
  * **self** (*object*)
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **include_onsite** (*bool*)
  * **just_one** (*bool*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[ *\_ScalarType_co*]]

#### *static* get_COOP(self, orbs, NN=None, include_onsite=False, spin=0)

Calculates the COHP for the given orbitals and nearest neighbors

**Parameters:**
: self (object): An object of the class COGITO_BAND or COGITO_UNIFORM
  orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  include_onsite (bool): Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms

**Returns:**
: npt.NDArray: returns COHP values in a [kpt,band] dimension

* **Parameters:**
  * **self** (*object*)
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **include_onsite** (*bool*)
  * **spin** (*int*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[ *\_ScalarType_co*]]

#### *static* get_mulliken_charge(self, elem)

* **Parameters:**
  * **self** (*object*)
  * **elem** (*str*)
* **Return type:**
  float

### COGITOico.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOico.complex128funs(phi, theta, sphharm_key)
