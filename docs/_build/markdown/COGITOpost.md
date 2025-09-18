# COGITOpost module

### *class* COGITOpost.COGITO_TB_Model(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False)

Bases: `object`

#### \_\_init_\_(directory: str, verbose: int = 0, file_suffix: str = '', orbs_orth: bool = False, spin_polar: bool = False) → None

Initializes the

* **Parameters:**
  * **directory** (`str`) – The path for the input files
  * **verbose** (`int`) – How much will be printed (0 is least)
  * **file_suffix** (`str`) – The suffix to the TBparams and overlaps files
  * **orbs_orth** (`bool`) – Whether the orbitals are orthogonal, if from COGITO this is always False

#### read_input(file: str = 'tb_input.txt') → None

#### read_TBparams(file: str = 'TBparams.txt') → None

#### read_overlaps(file: str = 'overlaps.txt') → None

#### read_orbitals(file: str = 'orbitals.npy') → None

This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.

* **Parameters:**
  **file** (`str`) – Orbital file

#### normalize_params()

#### set_hoppings(value: float, orb1: int, orb2: int, trans: tuple, spin: int = 0) → None

Change a TB parameter

* **Parameters:**
  * **value** (`float`) – The new parameter
  * **orb1** (`int`) – The first orbital index of the parameter
  * **orb2** (`int`) – The second orbital index of the parameter
  * **trans** (`tuple`) – The tuple of translation indices
* **Return type:**
  None

#### restrict_params(maximum_dist: float = 12.0, minimum_value: float = 0.0001) → None

Generates self.use_tbparams, self.use_overlaps, and self.use_vecs_to_orbs which are used in the gen_ham() funciton
With this, the calculation of hamiltonians by gen_ham() is both sparse and vectorized

* **Parameters:**
  * **maximum_dist** (`float`) – The maximmum distance between hopping parameters which should be included
  * **minimum_value** (`float`) – The minimum magnitude of hopping parameter which should be included

#### *static* make_orbitals(self, cartXYZ)

#### *static* plot_orbitals(self)

#### *static* generate_gpnts(self, kpt: list) → ndarray[tuple[int, ...], dtype[int64]]

similar to from pymatgen.io.vasp.outputs.Wavecar but is vectorized

* **Parameters:**
  **kpt** (`list`) – The k-point in reduced coordinates
* **Returns:**
  The gpoints
* **Return type:**
  npt.NDArray[

  ```
  np.int_
  ```

  ]

#### *static* get_ham(self: object, kpt: list, return_overlap: bool = False, return_truevec: bool = True, spin: int = 0) → list

This function generates the hamiltonian and overlap matrices for a given kpt.
Then it solves the generalized eigenvalue problem to return the eigvalues and vectors

* **Parameters:**
  * **self** (`object`) – An object with the attributes of the COGITO_TB_Model class
  * **kpt** (`list`) – The kpoint to regenerate at in reduced coordinates
  * **return_overlap** (`bool`) – If True, the function will also return the overlap matrix at the kpt; default is False
  * **return_truevec** (`bool`) – If True, the function will return the eigenvectors in the original nonorthogonal basis
    Default if True
  * **spin** (`int`) – The spin of the parameters for a spin-polarized calculation; default is 0–for non spin-polarized
* **Returns:**
  returns a list of the eigenvalues and eigenvectors (and overlap if return_overlap=True)
* **Return type:**
  list

#### *static* get_fullHam(self: object, kpt: list, spin: int = 0)

#### *static* get_neighbors(self) → list

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

#### *static* plot_crystal_field(self, atomnum: int = 0, orbitals: str = 'd', ylim: list = (-10, 0), spin: int = 0) → None

Plots the crystal field splitting diagram for the orbitals and atom given

* **Parameters:**
  * **atomnum** (`int`) – Which atom to plot for
  * **orbitals** (`str`) – Which orbitals to plot, “d” is most common
  * **ylim** (`list`) – The limits of the y-axis in the plot, will default to good value if left (-10,0)

#### *static* plot_hopping(self, spin: int = 0) → None

#### *static* plot_overlaps(self, spin: int = 0) → None

#### *static* compare_to_DFT(self, directory: str, extra_tag='') → list

This function reads the EIGENVAL from a DFT run, generates the energies from the TB model for the kpt grid,
And plots and compares the error between the TB model energies and DFT energies

* **Parameters:**
  * **self** (`unknown`) – An object of the class COGITO_TB_Model (can not be the BAND or UNIFORM classes!)
  * **directory** (`str`) – The directory where the EIGENVAL file is
* **Returns:**
  Returns a list of the (averaged over the valance bands) band distance (as defined by Marzari),
  : average maximum error, and average band error
* **Return type:**
  list

#### *static* get_COHP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COHP for the given orbitals and nearest neighbors

* **Parameters:**
  * **self** (`object`) – An object of the class COGITO_BAND or COGITO_UNIFORM
  * **orbs** (`dict`) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  * **NN** (`int`) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  * **include_onsite** (`bool`) – Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
  * **spin** (`int`) – The spin of the tight binding parameters; default is 0 works for nonspin-polarized
* **Returns:**
  returns COHP values in a [kpt,band] dimension
* **Return type:**
  npt.NDArray

#### *static* get_ICOHP(self, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

#### *static* get_COOP(self: object, orbs: dict, NN: int | None = None, include_onsite: bool = False, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

Calculates the COOP for the given orbitals and nearest neighbors

* **Parameters:**
  * **self** (`object`) – An object of the class COGITO_BAND or COGITO_UNIFORM
  * **orbs** (`dict`) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  * **NN** (`int`) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  * **include_onsite** (`bool`) – Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
  * **spin** (`int`) – The spin of the tight binding parameters; default is 0 works for nonspin-polarized
* **Returns:**
  returns COOP values in a [kpt,band] dimension
* **Return type:**
  npt.NDArray

#### *static* get_ICOOP(self, spin: int = 0) → ndarray[tuple[int, ...], dtype[\_ScalarType_co]]

### *class* COGITOpost.COGITO_BAND(TB_model: object, num_kpts: int = 100)

Bases: `object`

#### \_\_init_\_(TB_model: object, num_kpts: int = 100)

This class deals with all post-processing band structure analysis

* **Parameters:**
  **TB_model** (`object`) – requires an object of the class COGITO_TB_Model

#### get_bandstructure(num_kpts: int = 100) → None

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath

* **Parameters:**
  **num_kpts** (`int`) – The number of kpoints between EACH kpath
* **Returns:**
  Nothing
* **Return type:**
  None

#### plotBS(ax: object | None = None, ylim: list = (-10, 10), color_label: str = '', colors: ndarray[tuple[int, ...], dtype[\_ScalarType_co]] = np.array([]), colorhalf: float = 10) → object

* **Parameters:**
  * **ax** (`object`) – (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
  * **ylim** (`list`) – Limits on the y-axis of plot
  * **color_label** (`str`) – When being plotted from another function, this passes “COHP” or “COOP”
  * **colors** (`npt.NDArray`) – Magnitude for each point to use in color plotting, passed by get_COHP() function
  * **colorhalf** (`float`) – Sets scale of color bar
* **Returns:**
  matplotlib.pyplot axis with bandstructure plotted
* **Return type:**
  object

#### plotlyBS(ylim=(-10, 10), color_label='', colors=None, colorhalf=None, orbProj: bool = False) → object

Plots bandstructure (or projected bandstructure) using plotly graph_objects

* **Parameters:**
  * **ylim** (`unknown`) – Limits on the y-axis of plot
  * **color_label** (`unknown`) – When being plotted from another function, this passes “COHP” or “COOP”
  * **colors** (`unknown`) – Magnitude for each point to use in color plotting, passed by get_COHP() function
  * **colorhalf** (`unknown`) – Sets scale of color bar
* **Returns:**
  plotly figure with bandstructure plotted
* **Return type:**
  object

#### get_COHP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), colorhalf: float = 10, include_onsite: bool = False, from_dash: bool = False) → None

Calculates and plots the projected COHP values for each band and k-point on band structure

* **Parameters:**
  * **orbs** (`dict`) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  * **NN** (`int`) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  * **ylim** (`list`) – The limits of the y-axis (energy) of the band structure plot
  * **colorhalf** (`float`) – Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COHP)\*3
  * **include_onsite** (`bool`) – Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
  * **from_dash** (`bool`) – Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
* **Returns:**
  Nothing
* **Return type:**
  None

#### get_COOP(orbs: dict, NN: int | None = None, ylim: list = (-10, 10), colorhalf: float = 10, include_onsite: bool = False, from_dash=False, color_label: str = 'COOP', orbProj: bool = False) → None

Calculates and plots the projected COOP values for each band and k-point on band structure

* **Parameters:**
  * **orbs** (`dict`) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  * **NN** (`int`) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  * **ylim** (`list`) – The limits of the y-axis (energy) of the band structure plot
  * **colorhalf** (`float`) – Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COOP)\*3
  * **include_onsite** (`bool`) – Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
  * **from_dash** (`unknown`) – Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis
* **Returns:**
  Nothing
* **Return type:**
  None

#### get_projectedBS(orbdict: dict, ylim: list = (-10, 10), colorhalf: float = 10) → None

#### make_COHP_dashapp(pathname: str = '/COGITO_COHP/') → None

This function generate a dash app which allows the user to interactively select orbitals and nearest neighbors
to examine their project COHP band structure quickly

* **Parameters:**
  **pathname** (`str`) – Name appended to the default pathname for the html
* **Returns:**
  Nothing
* **Return type:**
  None

### *class* COGITOpost.COGITO_UNIFORM(TB_model: object, grid: tuple)

Bases: `object`

#### \_\_init_\_(TB_model: object, grid: tuple)

This class deals with all post-processing uniform grid analysis

* **Parameters:**
  **TB_model** (`object`) – requires an object of the class COGITO_TB_Model

#### get_uniform(grid: tuple) → None

* **Parameters:**
  **grid** (`tuple`) – The kpoint grid to use for the uniform sampling

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

* **Parameters:**
  * **atmind1** (`unknown`) – The atom number for the first atom
  * **atmind2** (`unknown`) – The atom number for the second atom
  * **center1** (`unknown`) – The center of the first atom (not using self.primATOMs)
  * **center2** (`unknown`) – The center of the second atom (not using self.primATOMs)
  * **orbCOOP** (`unknown`) – The orbCOOP which reveals how much of each orbital combo that is included in the bond.
    Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.
  * **cartXYZ** (`unknown`) – The 3D flattened grid that the bond density is calculated on
* **Returns:**
  A 1D array  (3D flattened) of the bond density
* **Return type:**
  unknown

#### get_bonds_figure_old(energy_cutoff: float = 0.1, offset: int = 0, plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

* **Parameters:**
  * **energy_cutoff** (`float`) – This is the minimum bond magnitude that will be plotted
  * **offset** (`int`) – The offset in the colors, set different values to try out different colors
  * **plot_atom** (`int`) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** (`bool`) – Whether only the atom defined in plot_atom should be plotted; default is False
  * **bond_max** (`float`) – The maximum bond distance that will be plotted outside the primitive cell
* **Returns:**
  Nothing
* **Return type:**
  None

#### get_bonds_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None) → None

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

* **Parameters:**
  * **energy_cutoff** (`float`) – This is the minimum bond magnitude that will be plotted
  * **bond_max** (`float`) – The maximum bond distance that will be plotted outside the primitive cell
  * **elem_colors** (`list`) – Colors for the elements based on order in tb_input. Length of list should be the number of
    unique elements. Can either be integer list to reference the default colors or list of
    plotly compatable colors.
  * **atom_colors** (`list`) – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** (`list`) – List of atom labels as a string.
  * **plot_atom** (`int`) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** (`bool`) – Whether only the atom defined in plot_atom should be plotted; default is False
  * **fovy** (`float`) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
  * **return_fig** (`bool`) – If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
  * **only_prim_atoms** (`bool`) – If True, only the atoms within the primitive cell are plotted.
    If False, atoms are added outside the primitive cell if the atom has a bond to an atom
    inside the primtive cell that meets energy_cutoff and bond_max criteria.
    Default is set in code False if self.numAtoms < 30, otherwise set to True
* **Returns:**
  Nothing
* **Return type:**
  None

#### get_bonds_charge_figure(energy_cutoff: float = 0.1, bond_max: float = 3.0, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, fovy: float = 10, return_fig: bool = False, only_prim_atoms: bool | None = None) → None

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label

* **Parameters:**
  * **energy_cutoff** (`float`) – This is the minimum bond magnitude that will be plotted
  * **bond_max** (`float`) – The maximum bond distance that will be plotted outside the primitive cell
  * **elem_colors** (`list`) – Colors for the elements based on order in tb_input. Length of list should be the number of
    unique elements. Can either be integer list to reference the default colors or list of
    plotly compatable colors.
  * **atom_colors** (`list`) – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** (`list`) – List of atom labels as a string.
  * **auto_label** (`str`) – Different options for plotting includes: (can include multiple in the string)
    “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
    “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
    “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
    “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
    NOTE: Only use “mulliken” OR “full”, NOT both
  * **plot_atom** (`int`) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** (`bool`) – Whether only the atom defined in plot_atom should be plotted; default is False
  * **fovy** (`float`) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
  * **return_fig** (`bool`) – If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object
  * **only_prim_atoms** (`bool`) – If True, only the atoms within the primitive cell are plotted.
    If False, atoms are added outside the primitive cell if the atom has a bond to an atom
    inside the primtive cell that meets energy_cutoff and bond_max criteria.
    Default is set in code False if self.numAtoms < 30, otherwise set to True
* **Returns:**
  Depend on return_fig parameter.
* **Return type:**
  None

#### get_bond_density_figure(energy_cutoff: float = 0.1, iso_max: float = 0.03, iso_min: float = -0.003, elem_colors: list = [], atom_colors: list = [], atom_labels: list = [], auto_label: str = '', plot_atom: int | None = None, one_atom: bool = False, bond_max: float = 3.0, fovy: float = 10, return_fig: bool = False) → None

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label

* **Parameters:**
  * **energy_cutoff** (`float`) – This is the minimum bond magnitude that will be plotted
  * **iso_max** (`float`) – The positive isosurface for plotting the bonds.
  * **iso_min** (`float`) – The negative isosurface for plotting the bonds.
  * **elem_colors** (`list`) – Colors for the elements based on order in tb_input. Length of list should be the number of
    unique elements. Can either be integer list to reference the default colors or list of
    plotly compatable colors.
  * **atom_colors** (`list`) – Colors for the atoms based on order in tb_input. Length of list should be the number of
    atoms in the primitive cell. Can either be integer list to reference the default colors or
    list of plotly compatable colors. If not set defaults to elem_colors.
  * **atom_labels** (`list`) – List of atom labels as a string.
  * **auto_label** (`str`) – Different options for plotting includes: (can include multiple in the string)
    “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
    “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
    “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
    “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
    NOTE: Only use “mulliken” OR “full”, NOT both
  * **plot_atom** (`int`) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  * **one_atom** (`bool`) – Whether only the atom defined in plot_atom should be plotted; default is False
  * **bond_max** (`float`) – The maximum bond distance that will be plotted outside the primitive cell
  * **fovy** (`float`) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
    Set between 3 (for close to orthographic) and 30 (for good perspective depth).
* **Returns:**
  Nothing, but saves plotly figure to ‘crystal_bonds.html’
* **Return type:**
  None

#### get_bond_info()

#### get_COHP_DOS_bybond(sigma=0.1, return_fig: bool = False)

#### get_crystal_plus_COHP(energy_cutoff: float = 0.05, bond_max: float = 3, auto_label: str = 'mulliken', fovy: float = 10) → None

The will plot the crystal bond plot on the left with interactivity to a COHP DOS plot on the right

* **Parameters:**
  * **energy_cutoff** (`float`) – This is the minimum bond magnitude that will be plotted
  * **bond_max** (`float`) – The maximum bond distance that will be plotted outside the primitive cell
  * **auto_label** (`str`) – Different options for plotting includes: (can include multiple in the string)
    “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
    “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
    “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
    “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
    NOTE: Only use “mulliken” OR “full”, NOT both
  * **fovy** (`float`) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
* **Returns:**
  Nothing, but saved to ‘bond_cohp_plot.html’
* **Return type:**
  None

#### *static* get_mulliken_charge(self: object, elem: str) → float

### *class* COGITOpost.COGITO_BS_widget(TB_model: object, num_kpts: int = 100)

Bases: `object`

#### \_\_init_\_(TB_model: object, num_kpts: int = 100)

This class deals with all post-processing band structure analysis

* **Parameters:**
  **TB_model** (`object`) – requires an object of the class COGITO_TB_Model

#### get_bandstructure(num_kpts: int = 100) → None

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath

* **Parameters:**
  **num_kpts** (`int`) – The number of kpoints between EACH kpath
* **Returns:**
  Nothing
* **Return type:**
  None

#### plotlyBS(ylim=(-10, 10), selectedDot=None, plotnew=False) → object

Plots bandstructure (or projected bandstructure) using plotly graph_objects

* **Parameters:**
  **ylim** (`unknown`) – Limits on the y-axis of plot
* **Returns:**
  plotly figure with bandstructure plotted
* **Return type:**
  object

#### plotBS(ax=None, selectedDot=None, plotnew=False, ylim=None)

* **Parameters:**
  * **ax** (`unknown`) – (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
  * **selectedDot** (`unknown`) – (1D integer array): gives kpoint and band index of the dot selected to make green circle
    eg: [3,4]
* **Returns:**
  matplotlib.pyplot axis with bandstructure plotted
* **Return type:**
  unknown

#### get_significant_bonds(band, kpoint, spin)

#### plot_bond_run(num_bond=0)

#### change_sig_bonds(old_vals, new_vals, tbvals=None, num_bond=None)

To change tight-binding parameter, need to know two orbitals and three translations

#### make_BS_widget(app=None)

### COGITOpost.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOpost.complex128funs(phi, theta, sphharm_key)
