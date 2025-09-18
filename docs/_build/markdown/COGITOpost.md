# COGITOpost module

### *class* COGITOpost.COGITO_TB_Model(directory, verbose=0, file_suffix='', orbs_orth=False, spin_polar=False)

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

#### read_TBparams(file='TBparams.txt')

* **Parameters:**
  **file** (*str*)
* **Return type:**
  None

#### read_overlaps(file='overlaps.txt')

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

#### normalize_params()

#### set_hoppings(value, orb1, orb2, trans, spin=0)

Change a TB parameter

**Parameters:**
: value (float): The new parameter
  orb1 (int): The first orbital index of the parameter
  orb2 (int): The second orbital index of the parameter
  trans (tuple): The tuple of translation indices

**Returns:**
: None:

* **Parameters:**
  * **value** (*float*)
  * **orb1** (*int*)
  * **orb2** (*int*)
  * **trans** (*tuple*)
  * **spin** (*int*)
* **Return type:**
  None

#### restrict_params(maximum_dist=12.0, minimum_value=0.0001)

Generates self.use_tbparams, self.use_overlaps, and self.use_vecs_to_orbs which are used in the gen_ham() funciton
With this, the calculation of hamiltonians by gen_ham() is both sparse and vectorized

**Parameters:**
: maximum_dist (float): The maximmum distance between hopping parameters which should be included
  minimum_value (float): The minimum magnitude of hopping parameter which should be included

* **Parameters:**
  * **maximum_dist** (*float*)
  * **minimum_value** (*float*)
* **Return type:**
  None

#### *static* make_orbitals(self, cartXYZ)

#### *static* plot_orbitals(self)

#### *static* generate_gpnts(self, kpt)

similar to from pymatgen.io.vasp.outputs.Wavecar but is vectorized

**Parameters:**
: kpt (list): The k-point in reduced coordinates

**Returns:**
: npt.NDArray[
  <br/>
  ```
  np.int_
  ```
  <br/>
  ]: The gpoints

* **Parameters:**
  **kpt** (*list*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[*int64*]]

#### *static* get_ham(self, kpt, return_overlap=False, return_truevec=True, spin=0)

This function generates the hamiltonian and overlap matrices for a given kpt.
Then it solves the generalized eigenvalue problem to return the eigvalues and vectors

**Parameters:**
: self (object): An object with the attributes of the COGITO_TB_Model class
  kpt (list): The kpoint to regenerate at in reduced coordinates
  return_overlap (bool): If True, the function will also return the overlap matrix at the kpt; default is False
  return_truevec (bool): If True, the function will return the eigenvectors in the original nonorthogonal basis
  <br/>
  > Default if True
  <br/>
  spin (int): The spin of the parameters for a spin-polarized calculation; default is 0–for non spin-polarized

**Returns:**
: list: returns a list of the eigenvalues and eigenvectors (and overlap if return_overlap=True)

* **Parameters:**
  * **self** (*object*)
  * **kpt** (*list*)
  * **return_overlap** (*bool*)
  * **return_truevec** (*bool*)
  * **spin** (*int*)
* **Return type:**
  list

#### *static* get_fullHam(self, kpt, spin=0)

* **Parameters:**
  * **self** (*object*)
  * **kpt** (*list*)
  * **spin** (*int*)

#### *static* get_neighbors(self)

This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.

* **Return type:**
  list

#### *static* plot_crystal_field(self, atomnum=0, orbitals='d', ylim=(-10, 0), spin=0)

Plots the crystal field splitting diagram for the orbitals and atom given

**Parameters:**
: atomnum (int): Which atom to plot for
  orbitals (str): Which orbitals to plot, “d” is most common
  ylim (list): The limits of the y-axis in the plot, will default to good value if left (-10,0)

* **Parameters:**
  * **atomnum** (*int*)
  * **orbitals** (*str*)
  * **ylim** (*list*)
  * **spin** (*int*)
* **Return type:**
  None

#### *static* plot_hopping(self, spin=0)

* **Parameters:**
  **spin** (*int*)
* **Return type:**
  None

#### *static* plot_overlaps(self, spin=0)

* **Parameters:**
  **spin** (*int*)
* **Return type:**
  None

#### *static* compare_to_DFT(self, directory, extra_tag='')

This function reads the EIGENVAL from a DFT run, generates the energies from the TB model for the kpt grid,
And plots and compares the error between the TB model energies and DFT energies

**Parameters:**
: self (unknown): An object of the class COGITO_TB_Model (can not be the BAND or UNIFORM classes!)
  directory (str): The directory where the EIGENVAL file is

**Returns:**
: list: Returns a list of the (averaged over the valance bands) band distance (as defined by Marzari),
  : average maximum error, and average band error

* **Parameters:**
  **directory** (*str*)
* **Return type:**
  list

#### *static* get_COHP(self, orbs, NN=None, include_onsite=False, spin=0)

Calculates the COHP for the given orbitals and nearest neighbors

**Parameters:**
: self (object): An object of the class COGITO_BAND or COGITO_UNIFORM
  orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  include_onsite (bool): Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
  spin (int): The spin of the tight binding parameters; default is 0 works for nonspin-polarized

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

#### *static* get_ICOHP(self, spin=0)

* **Parameters:**
  **spin** (*int*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[ *\_ScalarType_co*]]

#### *static* get_COOP(self, orbs, NN=None, include_onsite=False, spin=0)

Calculates the COOP for the given orbitals and nearest neighbors

**Parameters:**
: self (object): An object of the class COGITO_BAND or COGITO_UNIFORM
  orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  include_onsite (bool): Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
  spin (int): The spin of the tight binding parameters; default is 0 works for nonspin-polarized

**Returns:**
: npt.NDArray: returns COOP values in a [kpt,band] dimension

* **Parameters:**
  * **self** (*object*)
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **include_onsite** (*bool*)
  * **spin** (*int*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[ *\_ScalarType_co*]]

#### *static* get_ICOOP(self, spin=0)

* **Parameters:**
  **spin** (*int*)
* **Return type:**
  *ndarray*[tuple[int, …], *dtype*[ *\_ScalarType_co*]]

### *class* COGITOpost.COGITO_BAND(TB_model, num_kpts=100)

Bases: `object`

* **Parameters:**
  * **TB_model** (*object*)
  * **num_kpts** (*int*)

#### \_\_init_\_(TB_model, num_kpts=100)

This class deals with all post-processing band structure analysis

**Parameters:**
: TB_model (object): requires an object of the class COGITO_TB_Model

* **Parameters:**
  * **TB_model** (*object*)
  * **num_kpts** (*int*)

#### get_bandstructure(num_kpts=100)

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath

**Parameters:**
: num_kpts (int): The number of kpoints between EACH kpath

**Returns:**
: None: Nothing

* **Parameters:**
  **num_kpts** (*int*)
* **Return type:**
  None

#### plotBS(ax=None, ylim=(-10, 10), color_label='', colors=array([], dtype=float64), colorhalf=10)

**Parameters:**
ax (object): (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
ylim (list): Limits on the y-axis of plot
color_label (str): When being plotted from another function, this passes “COHP” or “COOP”
colors (npt.NDArray): Magnitude for each point to use in color plotting, passed by get_COHP() function
colorhalf (float): Sets scale of color bar

**Returns:**
object: matplotlib.pyplot axis with bandstructure plotted

* **Parameters:**
  * **ax** (*object* *|* *None*)
  * **ylim** (*list*)
  * **color_label** (*str*)
  * **colors** (*ndarray* *[**tuple* *[**int* *,*  *...* *]* *,* *dtype* *[* *\_ScalarType_co* *]* *]*)
  * **colorhalf** (*float*)
* **Return type:**
  object

#### plotlyBS(ylim=(-10, 10), color_label='', colors=None, colorhalf=None, orbProj=False)

Plots bandstructure (or projected bandstructure) using plotly graph_objects

**Parameters:**
: ylim (unknown): Limits on the y-axis of plot
  color_label (unknown): When being plotted from another function, this passes “COHP” or “COOP”
  colors (unknown): Magnitude for each point to use in color plotting, passed by get_COHP() function
  colorhalf (unknown): Sets scale of color bar

**Returns:**
: object: plotly figure with bandstructure plotted

* **Parameters:**
  **orbProj** (*bool*)
* **Return type:**
  object

#### get_COHP(orbs, NN=None, ylim=(-10, 10), colorhalf=10, include_onsite=False, from_dash=False)

Calculates and plots the projected COHP values for each band and k-point on band structure

**Parameters:**
: orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  ylim (list): The limits of the y-axis (energy) of the band structure plot
  colorhalf (float): Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COHP)\*3
  include_onsite (bool): Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms
  from_dash (bool): Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis

**Returns:**
: None: Nothing

* **Parameters:**
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **ylim** (*list*)
  * **colorhalf** (*float*)
  * **include_onsite** (*bool*)
  * **from_dash** (*bool*)
* **Return type:**
  None

#### get_COOP(orbs, NN=None, ylim=(-10, 10), colorhalf=10, include_onsite=False, from_dash=False, color_label='COOP', orbProj=False)

Calculates and plots the projected COOP values for each band and k-point on band structure

**Parameters:**
: orbs (dict): either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]
  NN (int): An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors
  ylim (list): The limits of the y-axis (energy) of the band structure plot
  colorhalf (float): Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COOP)\*3
  include_onsite (bool): Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure
  from_dash (unknown): Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis

**Returns:**
: None: Nothing

* **Parameters:**
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **ylim** (*list*)
  * **colorhalf** (*float*)
  * **include_onsite** (*bool*)
  * **color_label** (*str*)
  * **orbProj** (*bool*)
* **Return type:**
  None

#### get_projectedBS(orbdict, ylim=(-10, 10), colorhalf=10)

* **Parameters:**
  * **orbdict** (*dict*)
  * **ylim** (*list*)
  * **colorhalf** (*float*)
* **Return type:**
  None

#### make_COHP_dashapp(pathname='/COGITO_COHP/')

This function generate a dash app which allows the user to interactively select orbitals and nearest neighbors
to examine their project COHP band structure quickly

**Parameters:**
: pathname (str): Name appended to the default pathname for the html

**Returns:**
: None: Nothing

* **Parameters:**
  **pathname** (*str*)
* **Return type:**
  None

### *class* COGITOpost.COGITO_UNIFORM(TB_model, grid)

Bases: `object`

* **Parameters:**
  * **TB_model** (*object*)
  * **grid** (*tuple*)

#### \_\_init_\_(TB_model, grid)

This class deals with all post-processing uniform grid analysis

**Parameters:**
: TB_model (object): requires an object of the class COGITO_TB_Model

* **Parameters:**
  * **TB_model** (*object*)
  * **grid** (*tuple*)

#### get_uniform(grid)

**Parameters:**
grid (tuple): The kpoint grid to use for the uniform sampling

* **Parameters:**
  **grid** (*tuple*)
* **Return type:**
  None

#### recalc_efermi()

#### get_occupation(spin=0)

* **Parameters:**
  **spin** (*int*)

#### get_COHP(orbs, NN=None, ylim=(-10, 10), sigma=0.1, include_onsite=False)

* **Parameters:**
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **ylim** (*list*)
  * **include_onsite** (*bool*)

#### get_ICOHP()

#### save_ICOHP()

#### get_COOP(orbs, NN=None, ylim=(-10, 10), sigma=0.1, include_onsite=False, orbProj=False, label='')

* **Parameters:**
  * **orbs** (*dict*)
  * **NN** (*int* *|* *None*)
  * **ylim** (*list*)
  * **include_onsite** (*bool*)
  * **orbProj** (*bool*)
  * **label** (*str*)

#### get_projectedDOS(elem, ylim=(-10, 10), sigma=0.1, colorhalf=10)

* **Parameters:**
  * **elem** (*str*)
  * **ylim** (*list*)
  * **sigma** (*float*)
  * **colorhalf** (*float*)
* **Return type:**
  None

#### get_ICOOP()

#### save_ICOOP()

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

#### get_bonds_figure_old(energy_cutoff=0.1, offset=0, plot_atom=None, one_atom=False, bond_max=3.0)

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

**Parameters:**
: energy_cutoff (float): This is the minimum bond magnitude that will be plotted
  offset (int): The offset in the colors, set different values to try out different colors
  plot_atom (int): Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot
  one_atom (bool): Whether only the atom defined in plot_atom should be plotted; default is False
  bond_max (float): The maximum bond distance that will be plotted outside the primitive cell

**Returns:**
: None: Nothing

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **offset** (*int*)
  * **plot_atom** (*int* *|* *None*)
  * **one_atom** (*bool*)
  * **bond_max** (*float*)
* **Return type:**
  None

#### get_bonds_figure(energy_cutoff=0.1, bond_max=3.0, elem_colors=[], atom_colors=[], atom_labels=[], plot_atom=None, one_atom=False, fovy=10, return_fig=False, only_prim_atoms=None)

this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p

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
: None: Nothing

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **bond_max** (*float*)
  * **elem_colors** (*list*)
  * **atom_colors** (*list*)
  * **atom_labels** (*list*)
  * **plot_atom** (*int* *|* *None*)
  * **one_atom** (*bool*)
  * **fovy** (*float*)
  * **return_fig** (*bool*)
  * **only_prim_atoms** (*bool* *|* *None*)
* **Return type:**
  None

#### get_bonds_charge_figure(energy_cutoff=0.1, bond_max=3.0, elem_colors=[], atom_colors=[], atom_labels=[], auto_label='', plot_atom=None, one_atom=False, fovy=10, return_fig=False, only_prim_atoms=None)

Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label

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
* **Return type:**
  None

#### get_bond_density_figure(energy_cutoff=0.1, iso_max=0.03, iso_min=-0.003, elem_colors=[], atom_colors=[], atom_labels=[], auto_label='', plot_atom=None, one_atom=False, bond_max=3.0, fovy=10, return_fig=False)

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

#### get_COHP_DOS_bybond(sigma=0.1, return_fig=False)

* **Parameters:**
  **return_fig** (*bool*)

#### get_crystal_plus_COHP(energy_cutoff=0.05, bond_max=3, auto_label='mulliken', fovy=10)

The will plot the crystal bond plot on the left with interactivity to a COHP DOS plot on the right

**Parameters:**
: energy_cutoff (float): This is the minimum bond magnitude that will be plotted
  bond_max (float): The maximum bond distance that will be plotted outside the primitive cell
  auto_label (str): Different options for plotting includes: (can include multiple in the string)
  <br/>
  > “mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
  > “full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
  > “color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
  > “color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
  > NOTE: Only use “mulliken” OR “full”, NOT both
  <br/>
  fovy (float): field of view in the vertical direction. Use this tag to adjust depth perception in crystal.

**Returns:**
: None: Nothing, but saved to ‘bond_cohp_plot.html’

* **Parameters:**
  * **energy_cutoff** (*float*)
  * **bond_max** (*float*)
  * **auto_label** (*str*)
  * **fovy** (*float*)
* **Return type:**
  None

#### *static* get_mulliken_charge(self, elem)

* **Parameters:**
  * **self** (*object*)
  * **elem** (*str*)
* **Return type:**
  float

### *class* COGITOpost.COGITO_BS_widget(TB_model, num_kpts=100)

Bases: `object`

* **Parameters:**
  * **TB_model** (*object*)
  * **num_kpts** (*int*)

#### \_\_init_\_(TB_model, num_kpts=100)

This class deals with all post-processing band structure analysis

**Parameters:**
: TB_model (object): requires an object of the class COGITO_TB_Model

* **Parameters:**
  * **TB_model** (*object*)
  * **num_kpts** (*int*)

#### get_bandstructure(num_kpts=100)

The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath

**Parameters:**
: num_kpts (int): The number of kpoints between EACH kpath

**Returns:**
: None: Nothing

* **Parameters:**
  **num_kpts** (*int*)
* **Return type:**
  None

#### plotlyBS(ylim=(-10, 10), selectedDot=None, plotnew=False)

Plots bandstructure (or projected bandstructure) using plotly graph_objects

**Parameters:**
: ylim (unknown): Limits on the y-axis of plot

**Returns:**
: object: plotly figure with bandstructure plotted

* **Return type:**
  object

#### plotBS(ax=None, selectedDot=None, plotnew=False, ylim=None)

**Parameters:**
ax (unknown): (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis
selectedDot (unknown): (1D integer array): gives kpoint and band index of the dot selected to make green circle

> eg: [3,4]

**Returns:**
unknown: matplotlib.pyplot axis with bandstructure plotted

#### get_significant_bonds(band, kpoint, spin)

#### plot_bond_run(num_bond=0)

#### change_sig_bonds(old_vals, new_vals, tbvals=None, num_bond=None)

To change tight-binding parameter, need to know two orbitals and three translations

#### make_BS_widget(app=None)

### COGITOpost.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITOpost.complex128funs(phi, theta, sphharm_key)
