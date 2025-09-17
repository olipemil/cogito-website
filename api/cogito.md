---
layout: default
title: COGITO API Reference
nav_order: 2
parent: API Documentation
---

# COGITO API Reference

## Table of Contents

### Classes
- [COGITO](#cogito)

### Functions
- [func_for_rad](#func_for_rad)
- [func_for_rad_fit](#func_for_rad_fit)
- [func_for_rad_exp](#func_for_rad_exp)
- [lowdin_orth_vectors](#lowdin_orth_vectors)
- [lowdin_orth_vectors_orblap](#lowdin_orth_vectors_orblap)
- [GS_orth_twoLoworthSets](#gs_orth_twoloworthsets)
- [GS_orth_twoLoworthSets_orblap](#gs_orth_twoloworthsets_orblap)
- [GS_combine_states_orblap](#gs_combine_states_orblap)
- [complex128funs](#complex128funs)
- [normalize_wf](#normalize_wf)
- [periodic_integral_3d](#periodic_integral_3d)
- [reciprocal_integral](#reciprocal_integral)
- [_cart_to_red](#_cart_to_red)
- [_red_to_cart](#_red_to_cart)
- [smooth](#smooth)
- [extract_line_data](#extract_line_data)
- [combine_and_save_plots](#combine_and_save_plots)
- [plot_matrix](#plot_matrix)

## COGITO

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L23' target='_blank'>📂 View source code</a></div>

### Methods

#### __init__

```python
__init__(self, wavecar_dir, readmode, spin, spin_polar)
```

intialize the calculation
:param wavecar_dir - str: The directory with all the VASP output files
:param readmode - bool: If true, the code should have been run with readmode=False to generate output files;
                    will not read VASP output files or run orbital convergence and projection

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L24' target='_blank'>📍 View method source</a></div>

#### generate_TBmodel

```python
generate_TBmodel(self, irreducible_grid, verbose, include_excited, save_orb_data, save_orb_figs, plot_orbs, plot_projBS, plot_projDOS, calc_nrms, orbs, orbfactor, num_steps, num_outer, tag, min_proj, band_opt, orb_opt, orb_orth, start_from_orbnpy, minimum_orb_energy, min_duplicate_energy)
```

Runs all the functions neccessary to generate the TB interpolation.
REQUIRES UNIFORM KPT GRID WITH NO SYMMETRY OR FULL SYMMETRY FOR TB MODEL

:param irreducible_grid -- bool: Whether or not the kpoint grid is irreducible. True for ISYM=1|2|3; False for ISYM=-1 (does not work with ISYM=0)
:param verbose -- str: how much to ouput, includes 0,1,2,3. Higher numbers result in more output
:param include_excited -- int: how much to include excited orbital states, includes 0, 1, 2. To do this best avoid using POTCARs with semi-core states.
                            0 includes no excited orbital states (only ones which are partially occupied in isolated atom)
                            1 includes some excited states (if the POTCAR has the excited states + another higher one of the same l) (generally includes p orbital for d block)
                            2 includes maximally recommended states (condition of 1 + if the energy listed is the same as in isolated atom) (generally includes p orbitals for 1&2nd row)
:param plot_orbs -- bool: Plot the radial converged orbital being fit to Gaussian functions
:param plot_projBS -- bool: Plot the orbital projected bandstructure (not BS if the kpt grid is uniform)
:param plot_projDOS -- bool: Plot the orbital projected density of states (not correct DOS unless kpt grid is uniform)
:param orbs -- dictionary: The orbitals to plot the projection of. Defaults to all orbitals.
                FORMAT: {"element1":[orbital types]} e.g. {"Si":["s","p"],"C":["s","p"]}
:param minimum_orb_energy -- float: The lower limit to add semi-core states in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.
:param min_duplicate_energy -- float: The lower limit to add semi-core states when there is another valence state of the same l quantum number in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.

Recommended usage:
new_model = COGITO("silicon/")
new_model.generate_TBmodel(plot_orbs=True)

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L305' target='_blank'>📍 View method source</a></div>

#### test_initialorbs

```python
test_initialorbs(self, verbose, plot_orbs, include_excited, low_factor, high_factor, num_fac, num_outer, tag, min_proj, num_steps)
```

Tests dependance of orbital radius and quality on the size of initial orbitals.
Only runs the convergence of the orbitals without projecting them or generating the TB model

:param verbose -- str: how much to ouput, includes 0,1,2,3. Higher numbers result in more output
:param plot_orbs -- bool: Plot the radial converged orbital being fit to Gaussian functions
:param low_factor -- float: minimum to multiply the orbital size by; Default is 80%
:param high_factor -- float: maximum to multiply the orbital size by; Default is 120%
:param num_fac -- int: the number of steps between low_factor and high_factor to try

Recommended usage:
new_model = COGITO("silicon/")
new_model.generate_TBmodel(plot_orbs=True)

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L486' target='_blank'>📍 View method source</a></div>

#### get_WFdata_fromPOT

```python
get_WFdata_fromPOT(self)
```

Function which reads the pseudo and ae orbital information from the POTCAR
Creates the global variables self.atmProjectordata, self.atmRecipProjdata, and self.atmPsuedoAeData
FORMATs:
self.atmProjectordata [=] {"element",[float(cutoff_rad),{"orbtypes":[proj_real_radial_data]}]} e.g. {"Si",[1.45,{"s":[],"s_ex":[],"p":[],"p_ex":[]}}
self.atmRecipProjdata [=] {"element",[float(proj_gmax),{"orbtypes":[proj_recip_radial_data]}]}
self.atmPsuedoAeData [=] {"element",[radial_grid, {"orbtypes":[pseudo_radial_data]}}, {"orbtypes":[ae_radial_data]}]} e.g. {"Si,[[0,0.01,...,1.45],{"s":[],"s_ex":[],"p":[],"p_ex":[]},{"s":[],"s_ex":[],"p":[],"p_ex":[]}]

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L671' target='_blank'>📍 View method source</a></div>

#### get_orbs_fromPOT

```python
get_orbs_fromPOT(self, orbfactor)
```

Creates the 3D initial orbitals in real space from the pseudo radial orbitals.
Also sets the amount of orbitals by looping through atoms and their orbitals, thus intializes many orbital-dependent variables
:param orbfactor -- float: multipled by the radial part of the pseudo radial orbital to either shrink or grow them

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1166' target='_blank'>📍 View method source</a></div>

#### get_coefficients

```python
get_coefficients(self, orbitalWF, crystalWF, overlap_matrix, recip, band)
```

Find the coefficients for the amount of each pseudo orbital (Φ) in the pseudo wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an

:param orbitalWF -- dict of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
:param crystalWF -- dict of length N: All the DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF
:param overlap_matrix -- MxM matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence
:param recip -- bool: Whether the wavefunctions are defined in real or reciprocal space
:param band -- int: If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.

:return: The coefficients C_an of orbital a in band n

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1786' target='_blank'>📍 View method source</a></div>

#### get_aecoefficients

```python
get_aecoefficients(self, orbitalWF, crystalWF, aeoverlap_matrix, kpt, recip, band, full_kpt, prints, gpnts, set_gpnts)
```

Find the coefficients for the amount of each ae orbital (Φ) in the ae wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an
The orbital-wavefunction overlap is modified from the pseudo overlap using standard PAW methods

:param orbitalWF -- dict of length M: All the pseudo orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
:param crystalWF -- dict of length N: All the pseudo DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF
:param aeoverlap_matrix -- MxM matrix of complex float: The overlap of the ae orbitals. NOTE: The orbitals and their overlaps have a k-dependence
:param recip -- bool: Whether the wavefunctions are defined in real or reciprocal space
:param band -- int: If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.

:return: The coefficients C_na of orbital a in band n

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1829' target='_blank'>📍 View method source</a></div>

#### get_ae_overlap_matrix

```python
get_ae_overlap_matrix(self, orbitalWF, secondWF, secondisarray, recip, kpt)
```

Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ

:param orbitalWF -- dict of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
:param secondWF -- dict of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF
:param recip -- bool: Whether the orbitals are defined in real or reciprocal space

:return: The overlap matrix S_ab for orbitals a and b

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1915' target='_blank'>📍 View method source</a></div>

#### get_overlap_matrix

```python
get_overlap_matrix(self, orbitalWF, secondWF, secondisarray, recip)
```

Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ

:param orbitalWF -- dict of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
:param secondWF -- dict of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF
:param recip -- bool: Whether the orbitals are defined in real or reciprocal space

:return: The overlap matrix S_ab for orbitals a and b

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1996' target='_blank'>📍 View method source</a></div>

#### lowdin_orth

```python
lowdin_orth(self, low_orbitals, set_overlap, overlap, recip)
```

Orthogonalized the orbital based on the Lowdin scheme.
The new orbitals Ψ are defined by the original orbitals Φ as Ψ_b = conj(S_ab)^(-1/2)*Φ_a

:param low_orbitals -- dict of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors
:param set_overlap -- bool: Whether the orbital overlap is being passed to the function (True) or should be calculated (False)
:param overlap -- MxM matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence
:param recip -- bool: Whether the orbitals are defined in real or reciprocal space

:return: Lowdin orthogonalized orbitals

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2041' target='_blank'>📍 View method source</a></div>

#### converge_orbs_recip

```python
converge_orbs_recip(self, num_steps)
```

Converge to the atomic-like Bloch orbitals which best fit the DFT wavefunction
This procedes by ____

:param num_steps -- int: Maximum number of steps to perform the convergence;
                        Setting equal to 0 with run the standard direct algorithm where |X_a> = sum_n(c_na |Y_n>)
                        Where |Y_n> are the set of band (equal to number of orbitals) of the highest projection
                        
creates global variable one_orbitalWF which is referenced in the Bloch to atomic orbital fitting

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2077' target='_blank'>📍 View method source</a></div>

#### fit_to_atomic_orb

```python
fit_to_atomic_orb(self, plot_orbs)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2985' target='_blank'>📍 View method source</a></div>

#### spher_bessel_trans

```python
spher_bessel_trans(self, orbital_coeffs, rad_grid_size)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4082' target='_blank'>📍 View method source</a></div>

#### center_real_orbs

```python
center_real_orbs(self, real_orbs, kpt, make_real)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4118' target='_blank'>📍 View method source</a></div>

#### recip_to_real

```python
recip_to_real(self, recip_orbs, kpt, make_real)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4148' target='_blank'>📍 View method source</a></div>

#### real_to_recip

```python
real_to_recip(self, real_orbs, kpt)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4182' target='_blank'>📍 View method source</a></div>

#### get_kdep_recipprojs

```python
get_kdep_recipprojs(self, kpt, full_kpt, for_norm, gpnts, set_gpnts)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4213' target='_blank'>📍 View method source</a></div>

#### get_kdep_reciporbs

```python
get_kdep_reciporbs(self, kpt, full_kpt, gpnts, set_gpnts)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4316' target='_blank'>📍 View method source</a></div>

#### proj_all_kpoints

```python
proj_all_kpoints(self, max_bandavg, calc_nrms)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4370' target='_blank'>📍 View method source</a></div>

#### optimize_band_set

```python
optimize_band_set(self, band_opt, orb_opt, orb_orth)
```

:param kpt: disentangle for a certain kpt, if None do all kpts
:return: set of band which minimizes the difference between the orbital states left after and the band set orbital states;   maybe later: also minimize overlap between Lowdin orthogonalized band sets
outline:
start by finding the lowest band with projectibilty < 0.8
keep and lowdin orthogonailze everything beneath that band
discard any band with projectibility < 0.2
calculate 1-orbital states over all the good states > 0.8
calculate orbital states of each possible band
run through optimization

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4587' target='_blank'>📍 View method source</a></div>

#### expand_irred_kgrid

```python
expand_irred_kgrid(self)
```

this function does a couple things:
1. finds the kpoints of the reducible grid and the coorespond symmetry operations to get them from the irreducible points
2. creates the eigenvalues, eigenvectors, and overlaps matrices for the new reducible kpoint grid

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5019' target='_blank'>📍 View method source</a></div>

#### symmetrize_orbs

```python
symmetrize_orbs(self, recip_orbs)
```

This function is to symmetrize the iterated orbitals to decrease orbital mixing by ensuring orbital has s orbital symmetry

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5672' target='_blank'>📍 View method source</a></div>

#### get_Qab

```python
get_Qab(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5941' target='_blank'>📍 View method source</a></div>

#### get_ae_overlap_info

```python
get_ae_overlap_info(self, orbs, kpt, just_ae_overlap, recip, test, full_kpt, gpnts, set_gpnts)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5972' target='_blank'>📍 View method source</a></div>

#### get_orth_coeffs

```python
get_orth_coeffs(self, coeff, kpoint)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6191' target='_blank'>📍 View method source</a></div>

#### get_hamiltonian

```python
get_hamiltonian(self, kpoints)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6218' target='_blank'>📍 View method source</a></div>

#### make_fit_wannier

```python
make_fit_wannier(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6389' target='_blank'>📍 View method source</a></div>

#### get_TBparameter

```python
get_TBparameter(self, num_trans)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7123' target='_blank'>📍 View method source</a></div>

#### get_interp_ham

```python
get_interp_ham(self, kind, return_truevec, return_params)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7185' target='_blank'>📍 View method source</a></div>

#### get_neighbors

```python
get_neighbors(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7225' target='_blank'>📍 View method source</a></div>

#### orthogonalize_basis

```python
orthogonalize_basis(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7246' target='_blank'>📍 View method source</a></div>

#### get_offset

```python
get_offset(self, a)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7309' target='_blank'>📍 View method source</a></div>

#### write_TBfiles

```python
write_TBfiles(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7371' target='_blank'>📍 View method source</a></div>

#### write_recip_rad_orbs

```python
write_recip_rad_orbs(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7428' target='_blank'>📍 View method source</a></div>

#### read_recip_rad_orbs

```python
read_recip_rad_orbs(self, tag)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7466' target='_blank'>📍 View method source</a></div>

#### get_proj_on_aeorb

```python
get_proj_on_aeorb(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7478' target='_blank'>📍 View method source</a></div>

#### write_input_file

```python
write_input_file(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7521' target='_blank'>📍 View method source</a></div>

#### plot_BS

```python
plot_BS(self)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7554' target='_blank'>📍 View method source</a></div>

#### plot_projectedBS

```python
plot_projectedBS(self, orbs)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7565' target='_blank'>📍 View method source</a></div>

#### plot_projectedDOS

```python
plot_projectedDOS(self, orbs, xlim)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7600' target='_blank'>📍 View method source</a></div>

#### generate_gpnts

```python
generate_gpnts(self, kpt)
```

<div class='method-source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7664' target='_blank'>📍 View method source</a></div>

## func_for_rad

```python
func_for_rad(x, a, b, c, d, e, f, g, h, l)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7714' target='_blank'>📂 View source code</a></div>

## func_for_rad_fit

```python
func_for_rad_fit(x, a, b, con1, con2, con3, c, g, con4, l)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7717' target='_blank'>📂 View source code</a></div>

## func_for_rad_exp

```python
func_for_rad_exp(x, a, b, c, d, e, f, l)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7725' target='_blank'>📂 View source code</a></div>

## lowdin_orth_vectors

```python
lowdin_orth_vectors(vectors)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7728' target='_blank'>📂 View source code</a></div>

## lowdin_orth_vectors_orblap

```python
lowdin_orth_vectors_orblap(vectors, orblap, energies, return_energy)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7754' target='_blank'>📂 View source code</a></div>

## GS_orth_twoLoworthSets

```python
GS_orth_twoLoworthSets(vectors1, vectors2)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7800' target='_blank'>📂 View source code</a></div>

## GS_orth_twoLoworthSets_orblap

```python
GS_orth_twoLoworthSets_orblap(vectors1, vectors2, orblap, energy1, energy2, return_energy, energycut, ratio)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7826' target='_blank'>📂 View source code</a></div>

## GS_combine_states_orblap

```python
GS_combine_states_orblap(vectors1, vectors2, orblap, energy1, energy2, return_energy)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7895' target='_blank'>📂 View source code</a></div>

## complex128funs

```python
complex128funs(phi, theta, sphharm_key)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7956' target='_blank'>📂 View source code</a></div>

## normalize_wf

```python
normalize_wf(wavefunc, prim_vec, gridnum, return_integral, recip)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7979' target='_blank'>📂 View source code</a></div>

## periodic_integral_3d

```python
periodic_integral_3d(f, prim_vec, n, multiple_wfs)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7992' target='_blank'>📂 View source code</a></div>

## reciprocal_integral

```python
reciprocal_integral(f)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8032' target='_blank'>📂 View source code</a></div>

## _cart_to_red

```python
_cart_to_red(tmp, cart)
```

Convert cartesian vectors cart to reduced coordinates of a1,a2,a3 vectors

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8045' target='_blank'>📂 View source code</a></div>

## _red_to_cart

```python
_red_to_cart(prim_vec, prim_coord)
```

:param prim_vec: three float tuples representing the primitive vectors
:param prim_coord: list of float tuples for primitive coordinates
:return: list of float tuples for cartesian coordinates
        ex: cart_coord = _red_to_cart((a1,a2,a3),prim_coord)

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8061' target='_blank'>📂 View source code</a></div>

## smooth

```python
smooth(y, box_pts)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8076' target='_blank'>📂 View source code</a></div>

## extract_line_data

```python
extract_line_data(grid, gridXYZ, p1, p2, tolerance)
```

Extracts orbital magnitude along a line passing through p1 and p2 in a non-Cartesian 3D grid.

Parameters:
    grid (numpy.ndarray): 3D array of orbital magnitudes.
    gridXYZ (numpy.ndarray): 2D array (3, num_points) of real-space coordinates.
    p1 (tuple): First point (x1, y1, z1) in real space.
    p2 (tuple): Second point (x2, y2, z2) in real space.
    tolerance (float): Distance threshold to include points near the line.
    
Returns:
    distances (numpy.ndarray): Distances along the line.
    magnitudes (numpy.ndarray): Orbital magnitudes at corresponding distances.

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8082' target='_blank'>📂 View source code</a></div>

## combine_and_save_plots

```python
combine_and_save_plots(plots, filename, layout)
```

Combines multiple Matplotlib plots into a single figure and saves to a file.

Parameters:
    plots (list of matplotlib.figure.Figure): List of Matplotlib figures.
    filename (str): Output filename (supports .png, .pdf, .svg, etc.).
    layout (tuple or str): (rows, cols) for custom layout or "auto" for automatic grid.

Returns:
    None

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8130' target='_blank'>📂 View source code</a></div>

## plot_matrix

```python
plot_matrix(matrix, low_center, high_center, filename)
```

<div class='source-link'><a href='https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8179' target='_blank'>📂 View source code</a></div>

