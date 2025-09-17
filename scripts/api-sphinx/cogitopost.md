# COGITOpost Module

### *class* COGITOpost.COGITO_TB_Model(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False)

Bases: `object`

#### \_\_init_\_(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False) → None

Initializes the
@param directory: The path for the input files
@param verbose: How much will be printed (0 is least)
@param file_suffix: The suffix to the TBparams and overlaps files
@param orbs_orth: Whether the orbitals are orthogonal, if from COGITO this is always False

#### read_input(file: str = 'tb_input.txt') → None

#### read_TBparams(file: str = 'TBparams.txt') → None

#### read_overlaps(file: str = 'overlaps.txt') → None

#### read_orbitals(file: str = 'orbitals.npy') → None

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.
@param file: Orbital file

#### normalize_params()

#### set_hoppings(value: float, orb1: int, orb2: int, trans: tuple, spin: int = 0) → None

Change a TB parameter
@param value: The new parameter
@param orb1: The first orbital index of the parameter
@param orb2: The second orbital index of the parameter
@param trans: The tuple of translation indices
@return:

#### restrict_params(maximum_dist: float = 12.0, minimum_value: float = 0.0001) → None

Generates self.use_tbparams, self.use_overlaps, and self.use_vecs_to_orbs which are used in the gen_ham() funciton
With this, the calculation of hamiltonians by gen_ham() is both sparse and vectorized
@param maximum_dist: The maximmum distance between hopping parameters which should be included
@param minimum_value: The minimum magnitude of hopping parameter which should be included

#### *static* make_orbitals(self, cartXYZ)

#### *static* plot_orbitals(self)

#### *static* generate_gpnts(self, kpt: list) → ndarray[tuple[int, ...], dtype[int64]]

similar to from pymatgen.io.vasp.outputs.Wavecar but is vectorized
@param kpt: The k-point in reduced coordinates
@return: The gpoints

#### *static* get_ham(self: object, kpt: list, return_overlap: bool = False, return_truevec: bool = True, spin: int = 0) → list

This function generates the hamiltonian and overlap matrices for a given kpt.
Then it solves the generalized eigenvalue problem to return the eigvalues and vectors
@param self: An object with the attributes of the COGITO_TB_Model class
@param kpt: The kpoint to regenerate at in reduced coordinates
@param return_overlap: If True, the function will also return the overlap matrix at the kpt; default is False
@param return_truevec: If True, the function will return the eigenvectors in the original nonorthogonal basis

> Default if True

@param spin: The spin of the parameters for a spin-polarized calculation; default is 0–for non spin-polarized
@return: returns a list of the eigenvalues and eigenvectors (and overlap if return_overlap=True)

#### *static* get_fullHam(self: object, kpt: list, spin: int = 0)

#### *static* get_neighbors(self) → list

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

#### *static* plot_crystal_field(self, atomnum: int = 0, orbitals: str = 'd', ylim: list = (-10, 0), spin: int = 0) → None

Plots the crystal field splitting diagram for the orbitals and atom given
@param atomnum: Which atom to plot for
@param orbitals: Which orbitals to plot, “d” is most common
@param ylim: The limits of the y-axis in the plot, will default to good value if left (-10,0)

#### *static* plot_hopping(self, spin: int = 0) → None

#### *static* plot_overlaps(self, spin: int = 0) → None

#### *static* compare_to_DFT(self, directory: str, extra_tag='') → list

This function reads the EIGENVAL from a DFT run, generates the energies from the TB model for the kpt grid,
And plots and compares the error between the TB model energies and DFT energies
@param self: An object of the class COGITO_TB_Model (can not be the BAND or UNIFORM classes!)
@param directory: The directory where the EIGENVAL file is
@return: Returns a list of the (averaged over the valance bands) band distance (as defined by Marzari),

> average maximum error, and average band error

#### *static* get_COHP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@param spin: The spin of the tight binding parameters; default is 0 works for nonspin-polarized
@return: returns COHP values in a [kpt,band] dimension

#### *static* get_ICOHP(self, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

#### *static* get_COOP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COOP for the given orbitals and nearest neighbors
@param self: An object of the class COGITO_BAND or COGITO_UNIFORM
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param include_onsite: Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
@param spin: The spin of the tight binding parameters; default is 0 works for nonspin-polarized
@return: returns COOP values in a [kpt,band] dimension

#### *static* get_ICOOP(self, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

### *class* COGITOpost.COGITO_BAND(TB_model: object, num_kpts: int = 100)

Bases: `object`

#### \_\_init_\_(TB_model: object, num_kpts: int = 100)

This class deals with all post-processing band structure analysis
@param TB_model: requires an object of the class COGITO_TB_Model

#### get_bandstructure(num_kpts: int = 100) → None

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath
@param num_kpts: The number of kpoints between EACH kpath
@return: Nothing

#### plotBS(ax: object | None = None, ylim: list = (-10, 10), color_label: str = '', colors: ndarray[tuple[int, ...], dtype[\_ScalarType_co]] = array([], dtype=float64), colorhalf: float = 10) → object

@param ax (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
@param ylim: Limits on the y-axis of plot
@param color_label: When being plotted from another function, this passes “COHP” or “COOP”
@param colors: Magnitude for each point to use in color plotting, passed by get_COHP() function
@param colorhalf: Sets scale of color bar
@return: matplotlib.pyplot axis with bandstructure plotted

#### plotlyBS(ylim=(-10, 10), color_label='', colors=None, colorhalf=None, orbProj: bool = False) → object

Plots bandstructure (or projected bandstructure) using plotly graph_objects
@param ylim: Limits on the y-axis of plot
@param color_label: When being plotted from another function, this passes “COHP” or “COOP”
@param colors: Magnitude for each point to use in color plotting, passed by get_COHP() function
@param colorhalf: Sets scale of color bar
@return: plotly figure with bandstructure plotted

#### get_COHP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), colorhalf: float = 10, include_onsite: bool = False, from_dash: bool = False) → None

Calculates and plots the projected COHP values for each band and k-point on band structure
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param ylim: The limits of the y-axis (energy) of the band structure plot
@param colorhalf: Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COHP)\*3
@param include_onsite: Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
@param from_dash: Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
@return: Nothing

#### get_COOP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), colorhalf: float = 10, include_onsite: bool = False, from_dash=False, color_label: str = 'COOP', orbProj: bool = False) → None

Calculates and plots the projected COOP values for each band and k-point on band structure
@param orbs: either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
@param NN: An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
@param ylim: The limits of the y-axis (energy) of the band structure plot
@param colorhalf: Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COOP)\*3
@param include_onsite: Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
@param from_dash: Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
@return: Nothing

#### get_projectedBS(orbdict: dict, ylim: list = (-10, 10), colorhalf: float = 10) → None

#### make_COHP_dashapp(pathname: str = '/COGITO_COHP/') → None

This function generate a dash app which allows the user to interactively select orbitals and nearest neighbors
to examine their project COHP band structure quickly
@param pathname: Name appended to the default pathname for the html
@return: Nothing

### *class* COGITOpost.COGITO_UNIFORM(TB_model: object, grid: tuple)

Bases: `object`

#### \_\_init_\_(TB_model: object, grid: tuple)

This class deals with all post-processing uniform grid analysis
@param TB_model: requires an object of the class COGITO_TB_Model

#### get_uniform(grid: tuple) → None

@param grid: The kpoint grid to use for the uniform sampling

#### recalc_efermi()

#### get_occupation(spin: int = 0)

#### get_COHP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), sigma=0.1, include_onsite: bool = False)

#### get_ICOHP()

#### save_ICOHP()

#### get_COOP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), sigma=0.1, include_onsite: bool = False, orbProj: bool = False, label: str = '')

#### get_projectedDOS(elem: str, ylim: list = (-10, 10), sigma: float = 0.1, colorhalf: float = 10) → None

#### get_ICOOP()

#### save_ICOOP()

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

#### get_bonds_figure_old(energy_cutoff: float = 0.1, offset: int = 0, plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param offset: The offset in the colors, set different values to try out different colors
@param plot_atom: Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@return: Nothing

#### get_bonds_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None) → None

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
@param plot_atom: Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
@param one_atom: Whether only the atom defined in plot_atom should be plotted; default is False
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

> Set between 3 (for close to orthographic) and 30 (for good perspective depth).

@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.

> If False, atoms are added outside the primitive cell if the atom has a bond to an atom
> inside the primtive cell that meets energy_cutoff and bond_max criteria.
> Default is set in code False if self.numAtoms < 30, otherwise set to True

@return: Nothing

#### get_bonds_charge_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None) → None

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
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
@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

> Set between 3 (for close to orthographic) and 30 (for good perspective depth).

@param return_fig: If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
@param only_prim_atoms: If True, only the atoms within the primitive cell are plotted.

> If False, atoms are added outside the primitive cell if the atom has a bond to an atom
> inside the primtive cell that meets energy_cutoff and bond_max criteria.
> Default is set in code False if self.numAtoms < 30, otherwise set to True

@return: Depend on return_fig parameter.

#### get_bond_density_figure(energy_cutoff: float = 0.1, iso_max: float = 0.03, iso_min: float = -0.003, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

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

#### get_COHP_DOS_bybond(sigma=0.1, return_fig: bool = False)

#### get_crystal_plus_COHP(energy_cutoff: float = 0.05, bond_max: float = 3, auto_label: str = 'mulliken', fovy: float = 10) → None

The will plot the crystal bond plot on the left with interactivity to a COHP DOS plot on the right
@param energy_cutoff: This is the minimum bond magnitude that will be plotted
@param bond_max: The maximum bond distance that will be plotted outside the primitive cell
@param auto_label: Different options for plotting includes: (can include multiple in the string)

> “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
> “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
> “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
> “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
> NOTE: Only use “mulliken” OR “full”, NOT both

@param fovy: field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
@return: Nothing, but saved to ‘bond_cohp_plot.html’

#### *static* get_mulliken_charge(self: object, elem: str) → float

### *class* COGITOpost.COGITO_BS_widget(TB_model: object, num_kpts: int = 100)

Bases: `object`

#### \_\_init_\_(TB_model: object, num_kpts: int = 100)

This class deals with all post-processing band structure analysis
@param TB_model: requires an object of the class COGITO_TB_Model

#### get_bandstructure(num_kpts: int = 100) → None

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath
@param num_kpts: The number of kpoints between EACH kpath
@return: Nothing

#### plotlyBS(ylim=(-10, 10), selectedDot=None, plotnew=False) → object

Plots bandstructure (or projected bandstructure) using plotly graph_objects
@param ylim: Limits on the y-axis of plot
@return: plotly figure with bandstructure plotted

#### plotBS(ax=None, selectedDot=None, plotnew=False, ylim=None)

* **Parameters:**
  * **axis****)** (*ax* *(**matplotlib.pyplot*) – axis to save the bandstructure to, otherwise generate new axis
  * **array****)** (*selectedDot* *(**1D integer*) – gives kpoint and band index of the dot selected to make green circle
    eg: [3,4]
* **Returns:**
  matplotlib.pyplot axis with bandstructure plotted

#### get_significant_bonds(band, kpoint, spin)

#### plot_bond_run(num_bond=0)

#### change_sig_bonds(old_vals, new_vals, tbvals=None, num_bond=None)

To change tight-binding parameter, need to know two orbitals and three translations

#### make_BS_widget(app=None)

### COGITOpost.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOpost.complex128funs(phi, theta, sphharm_key)
