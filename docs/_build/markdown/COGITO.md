# COGITO module

### *class* COGITO.COGITO(wavecar_dir, readmode=False, spin=0, spin_polar=False)

Bases: `object`

#### \_\_init_\_(wavecar_dir, readmode=False, spin=0, spin_polar=False)

intialize the calculation

**Parameters:**
: wavecar_dir (str): The directory with all the VASP output files
  readmode (bool): If true, the code should have been run with readmode=False to generate output files;
  <br/>
  > will not read VASP output files or run orbital convergence and projection

#### generate_TBmodel(irreducible_grid=True, verbose=0, include_excited=1, save_orb_data=True, save_orb_figs=False, plot_orbs=False, plot_projBS=False, plot_projDOS=False, calc_nrms=False, orbs=None, orbfactor=1.0, num_steps=50, num_outer=3, tag='', min_proj=0.02, band_opt=True, orb_opt=True, orb_orth=False, start_from_orbnpy=False, minimum_orb_energy=-60, min_duplicate_energy=-60)

Runs all the functions neccessary to generate the TB interpolation.
REQUIRES UNIFORM KPT GRID WITH NO SYMMETRY OR FULL SYMMETRY FOR TB MODEL

**Parameters:**
: irreducible_grid (bool): Whether or not the kpoint grid is irreducible. True for ISYM=1|2|3; False for ISYM=-1 (does not work with ISYM=0)
  verbose (str): how much to ouput, includes 0,1,2,3. Higher numbers result in more output
  include_excited (int): how much to include excited orbital states, includes 0, 1, 2. To do this best avoid using POTCARs with semi-core states.
  <br/>
  > 0 includes no excited orbital states (only ones which are partially occupied in isolated atom)
  > 1 includes some excited states (if the POTCAR has the excited states + another higher one of the same l) (generally includes p orbital for d block)
  > 2 includes maximally recommended states (condition of 1 + if the energy listed is the same as in isolated atom) (generally includes p orbitals for 1&2nd row)
  <br/>
  plot_orbs (bool): Plot the radial converged orbital being fit to Gaussian functions
  plot_projBS (bool): Plot the orbital projected bandstructure (not BS if the kpt grid is uniform)
  plot_projDOS (bool): Plot the orbital projected density of states (not correct DOS unless kpt grid is uniform)
  orbs (dictionary): The orbitals to plot the projection of. Defaults to all orbitals.
  <br/>
  > FORMAT: {“element1”:[orbital types]} e.g. {“Si”:[“s”,”p”],”C”:[“s”,”p”]}
  <br/>
  minimum_orb_energy (float): The lower limit to add semi-core states in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.
  min_duplicate_energy (float): The lower limit to add semi-core states when there is another valence state of the same l quantum number in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.
  <br/>
  Usage:
  new_model = COGITO(“silicon/”)
  new_model.generate_TBmodel(plot_orbs=True)

* **Parameters:**
  * **minimum_orb_energy** (*float*)
  * **min_duplicate_energy** (*float*)

#### test_initialorbs(verbose=0, plot_orbs=False, include_excited=1, low_factor=0.8, high_factor=1.2, num_fac=9, num_outer=2, tag='', min_proj=0.02, num_steps=50, minimum_orb_energy=-60, min_duplicate_energy=-60)

Tests dependance of orbital radius and quality on the size of initial orbitals.
Only runs the convergence of the orbitals without projecting them or generating the TB model

**Parameters:**
: verbose (str): how much to ouput, includes 0,1,2,3. Higher numbers result in more output
  plot_orbs (bool): Plot the radial converged orbital being fit to Gaussian functions
  low_factor (float): minimum to multiply the orbital size by; Default is 80%
  high_factor (float): maximum to multiply the orbital size by; Default is 120%
  num_fac (int): the number of steps between low_factor and high_factor to try
  <br/>
  Usage:
  new_model = COGITO(“silicon/”)
  new_model.generate_TBmodel(plot_orbs=True)

* **Parameters:**
  * **minimum_orb_energy** (*float*)
  * **min_duplicate_energy** (*float*)

#### get_WFdata_fromPOT()

Function which reads the pseudo and ae orbital information from the POTCAR
Creates the global variables self.atmProjectordata, self.atmRecipProjdata, and self.atmPsuedoAeData
FORMATs:
self.atmProjectordata [=] {“element”,[float(cutoff_rad),{“orbtypes”:[proj_real_radial_data]}]} e.g. {“Si”,[1.45,{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]}}
self.atmRecipProjdata [=] {“element”,[float(proj_gmax),{“orbtypes”:[proj_recip_radial_data]}]}
self.atmPsuedoAeData [=] {“element”,[radial_grid, {“orbtypes”:[pseudo_radial_data]}}, {“orbtypes”:[ae_radial_data]}]} e.g. {“Si,[[0,0.01,…,1.45],{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]},{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]}]

#### get_orbs_fromPOT(orbfactor=1.0)

Creates the 3D initial orbitals in real space from the pseudo radial orbitals.
Also sets the amount of orbitals by looping through atoms and their orbitals, thus intializes many orbital-dependent variables

**Parameters:**
: orbfactor (float): multipled by the radial part of the pseudo radial orbital to either shrink or grow them

#### get_coefficients(orbitalWF, crystalWF, overlap_matrix, recip=False, band=None)

Find the coefficients for the amount of each pseudo orbital (Φ) in the pseudo wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa\*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab\*C_bn = O_an

* **Returns:**
  The coefficients C_an of orbital a in band n

**Parameters:**
: orbitalWF (dict): of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
  crystalWF (dict): of length N: All the DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF
  overlap_matrix (MxM): matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence
  recip (bool): Whether the wavefunctions are defined in real or reciprocal space
  band (int): If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.

#### get_aecoefficients(orbitalWF, crystalWF, aeoverlap_matrix, kpt, recip=False, band=None, full_kpt=False, prints=False, gpnts=None, set_gpnts=False)

Find the coefficients for the amount of each ae orbital (Φ) in the ae wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa\*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab\*C_bn = O_an
The orbital-wavefunction overlap is modified from the pseudo overlap using standard PAW methods

* **Returns:**
  The coefficients C_na of orbital a in band n

**Parameters:**
: orbitalWF (dict): of length M: All the pseudo orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
  crystalWF (dict): of length N: All the pseudo DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF
  aeoverlap_matrix (MxM): matrix of complex float: The overlap of the ae orbitals. NOTE: The orbitals and their overlaps have a k-dependence
  recip (bool): Whether the wavefunctions are defined in real or reciprocal space
  band (int): If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.

#### get_ae_overlap_matrix(orbitalWF, secondWF=None, secondisarray=False, recip=True, kpt=0)

Finds the overlap matrix S_ab = Φa\*φb. If secondWF is not defined, φ = Φ

* **Returns:**
  The overlap matrix S_ab for orbitals a and b

**Parameters:**
: orbitalWF (dict): of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
  secondWF (dict): of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF
  recip (bool): Whether the orbitals are defined in real or reciprocal space

#### get_overlap_matrix(orbitalWF, secondWF=None, secondisarray=False, recip=False)

Finds the overlap matrix S_ab = Φa\*φb. If secondWF is not defined, φ = Φ

* **Returns:**
  The overlap matrix S_ab for orbitals a and b

**Parameters:**
: orbitalWF (dict): of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
  secondWF (dict): of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF
  recip (bool): Whether the orbitals are defined in real or reciprocal space

#### lowdin_orth(low_orbitals, set_overlap=False, overlap=None, recip=False)

Orthogonalized the orbital based on the Lowdin scheme.
The new orbitals Ψ are defined by the original orbitals Φ as Ψ_b = conj(S_ab)^(-1/2)\*Φ_a

* **Returns:**
  Lowdin orthogonalized orbitals

**Parameters:**
: low_orbitals (dict): of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
  set_overlap (bool): Whether the orbital overlap is being passed to the function (True) or should be calculated (False)
  overlap (MxM): matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence
  recip (bool): Whether the orbitals are defined in real or reciprocal space

#### converge_orbs_recip(num_steps=50)

Converge to the atomic-like Bloch orbitals which best fit the DFT wavefunction
This procedes by \_\_\_\_

creates global variable one_orbitalWF which is referenced in the Bloch to atomic orbital fitting

**Parameters:**
: num_steps (int): Maximum number of steps to perform the convergence;
  : Setting equal to 0 with run the standard direct algorithm where 
    <br/>
    ```
    |
    ```
    <br/>
    X_a> = sum_n(c_na 
    <br/>
    ```
    |
    ```
    <br/>
    Y_n>)
    Where 
    <br/>
    ```
    |
    ```
    <br/>
    Y_n> are the set of band (equal to number of orbitals) of the highest projection

#### fit_to_atomic_orb(plot_orbs=False)

#### spher_bessel_trans(orbital_coeffs, rad_grid_size=500)

#### center_real_orbs(real_orbs, kpt=0, make_real=False)

#### recip_to_real(recip_orbs, kpt=0, make_real=False)

#### real_to_recip(real_orbs, kpt=0)

#### get_kdep_recipprojs(kpt, full_kpt=False, for_norm=False, gpnts=None, set_gpnts=False)

#### get_kdep_reciporbs(kpt, full_kpt=False, gpnts=None, set_gpnts=False)

#### proj_all_kpoints(max_bandavg=None, calc_nrms=False)

#### optimize_band_set(band_opt=True, orb_opt=True, orb_orth=False)

* **Returns:**
  set of band which minimizes the difference between the orbital states left after and the band set orbital states;   maybe later: also minimize overlap between Lowdin orthogonalized band sets

outline:
start by finding the lowest band with projectibilty < 0.8
keep and lowdin orthogonailze everything beneath that band
discard any band with projectibility < 0.2
calculate 1-orbital states over all the good states > 0.8
calculate orbital states of each possible band
run through optimization

#### expand_irred_kgrid()

this function does a couple things:
1. finds the kpoints of the reducible grid and the coorespond symmetry operations to get them from the irreducible points
2. creates the eigenvalues, eigenvectors, and overlaps matrices for the new reducible kpoint grid

#### symmetrize_orbs(recip_orbs)

This function is to symmetrize the iterated orbitals to decrease orbital mixing by ensuring orbital has s orbital symmetry

#### get_Qab()

#### get_ae_overlap_info(orbs=None, kpt=0, just_ae_overlap=False, recip=False, test=False, full_kpt=False, gpnts=None, set_gpnts=False)

#### get_orth_coeffs(coeff, kpoint=None)

#### get_hamiltonian(kpoints=None)

#### make_fit_wannier()

#### get_TBparameter(num_trans=5)

#### get_interp_ham(kind, return_truevec=True, return_params=False)

#### get_neighbors()

#### orthogonalize_basis()

#### get_offset(a=2)

#### write_TBfiles()

#### write_recip_rad_orbs()

#### read_recip_rad_orbs(tag='')

#### get_proj_on_aeorb()

#### write_input_file()

#### plot_BS()

#### plot_projectedBS(orbs)

#### plot_projectedDOS(orbs, xlim=None)

#### generate_gpnts(kpt)

### COGITO.func_for_rad(x, a, b, c, d, e, f, g, h, l)

### COGITO.func_for_rad_fit(x, a, b, con1, con2, con3, c, g, con4, l)

### COGITO.func_for_rad_exp(x, a, b, c, d, e, f, l)

### COGITO.lowdin_orth_vectors(vectors)

### COGITO.lowdin_orth_vectors_orblap(vectors, orblap, energies=None, return_energy=False)

### COGITO.GS_orth_twoLoworthSets(vectors1, vectors2)

### COGITO.GS_orth_twoLoworthSets_orblap(vectors1, vectors2, orblap, energy1=None, energy2=None, return_energy=False, energycut=0, ratio=[])

### COGITO.GS_combine_states_orblap(vectors1, vectors2, orblap, energy1=None, energy2=None, return_energy=False)

### COGITO.complex128funs(phi, theta, sphharm_key)

### COGITO.normalize_wf(wavefunc, prim_vec, gridnum, return_integral=False, recip=False)

### COGITO.periodic_integral_3d(f, prim_vec, n, multiple_wfs=False)

### COGITO.reciprocal_integral(f)

### COGITO.smooth(y, box_pts)

### COGITO.extract_line_data(grid, gridXYZ, p1, p2, tolerance=0.5)

Extracts orbital magnitude along a line passing through p1 and p2 in a non-Cartesian 3D grid.

* **Parameters:**
  * **grid** (*numpy.ndarray*) – 3D array of orbital magnitudes.
  * **gridXYZ** (*numpy.ndarray*) – 2D array (3, num_points) of real-space coordinates.
  * **p1** (*tuple*) – First point (x1, y1, z1) in real space.
  * **p2** (*tuple*) – Second point (x2, y2, z2) in real space.
  * **tolerance** (*float*) – Distance threshold to include points near the line.
* **Returns:**
  Distances along the line.
  magnitudes (numpy.ndarray): Orbital magnitudes at corresponding distances.
* **Return type:**
  distances (numpy.ndarray)

### COGITO.combine_and_save_plots(plots, filename='combined_plot.png', layout=None)

Combines multiple Matplotlib plots into a single figure and saves to a file.

* **Parameters:**
  * **plots** (*list* *of* *matplotlib.figure.Figure*) – List of Matplotlib figures.
  * **filename** (*str*) – Output filename (supports .png, .pdf, .svg, etc.).
  * **layout** (*tuple* *or* *str*) – (rows, cols) for custom layout or “auto” for automatic grid.
* **Returns:**
  None

### COGITO.plot_matrix(matrix, low_center=0.2, high_center=0.85, filename='matrix.png')
