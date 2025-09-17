---
layout: default
title: COGITO API Reference
nav_order: 2
parent: API Documentation
---

# COGITO API Reference

<div class="api-module-header">
    <p class="module-description">API reference for the COGITO module</p>
    <div class="source-link">
        <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py" target="_blank">View Source</a>
    </div>
</div>

<div class="api-tabs">
    <div class="tab-buttons">
        <button class="tab-btn active" onclick="showTab('classes')">Classes</button>
        <button class="tab-btn" onclick="showTab('functions')">Functions</button>
    </div>

    <div id="classes" class="tab-content active">

        <div class="class-section" id="cogito">
            <div class="class-header">
                <h2>class COGITO</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L23" target="_blank">source</a>
                </div>
            </div>

            <div class="methods-section">
                <h3>Methods</h3>
                <div class="methods-list">

                    <div class="method" id="__init__">
                        <div class="method-header">
                            <h4>__init__</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L24" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>__init__(self, wavecar_dir, readmode=False, spin=0, spin_polar=False)</code>
                        </div>

                        <div class="method-description">
                            <p>intialize the calculation
will not read VASP output files or run orbital convergence and projection</p>
                        </div>
                    </div>

                    <div class="method" id="generate_TBmodel">
                        <div class="method-header">
                            <h4>generate_TBmodel</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L305" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>generate_TBmodel(self, irreducible_grid=True, verbose=0, include_excited=1, save_orb_data=True, save_orb_figs=False, plot_orbs=False, plot_projBS=False, plot_projDOS=False, calc_nrms=False, orbs=None, orbfactor=1.0, num_steps=50, num_outer=3, tag='', min_proj=0.02, band_opt=True, orb_opt=True, orb_orth=False, start_from_orbnpy=False, minimum_orb_energy=..., min_duplicate_energy=...)</code>
                        </div>

                        <div class="method-description">
                            <p>Runs all the functions neccessary to generate the TB interpolation.
REQUIRES UNIFORM KPT GRID WITH NO SYMMETRY OR FULL SYMMETRY FOR TB MODEL
0 includes no excited orbital states (only ones which are partially occupied in isolated atom)
1 includes some excited states (if the POTCAR has the excited states + another higher one of the same l) (generally includes p orbital for d block)
2 includes maximally recommended states (condition of 1 + if the energy listed is the same as in isolated atom) (generally includes p orbitals for 1&2nd row)
FORMAT: {"element1":[orbital types]} e.g. {"Si":["s","p"],"C":["s","p"]}
Recommended usage:
new_model = COGITO("silicon/")
new_model.generate_TBmodel(plot_orbs=True)</p>
                        </div>
                    </div>

                    <div class="method" id="test_initialorbs">
                        <div class="method-header">
                            <h4>test_initialorbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L486" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>test_initialorbs(self, verbose=0, plot_orbs=False, include_excited=1, low_factor=0.8, high_factor=1.2, num_fac=9, num_outer=2, tag='', min_proj=0.02, num_steps=50)</code>
                        </div>

                        <div class="method-description">
                            <p>Tests dependance of orbital radius and quality on the size of initial orbitals.
Only runs the convergence of the orbitals without projecting them or generating the TB model
Recommended usage:
new_model = COGITO("silicon/")
new_model.generate_TBmodel(plot_orbs=True)</p>
                        </div>
                    </div>

                    <div class="method" id="get_WFdata_fromPOT">
                        <div class="method-header">
                            <h4>get_WFdata_fromPOT</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L671" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_WFdata_fromPOT(self)</code>
                        </div>

                        <div class="method-description">
                            <p>Function which reads the pseudo and ae orbital information from the POTCAR
Creates the global variables self.atmProjectordata, self.atmRecipProjdata, and self.atmPsuedoAeData
FORMATs:
self.atmProjectordata [=] {"element",[float(cutoff_rad),{"orbtypes":[proj_real_radial_data]}]} e.g. {"Si",[1.45,{"s":[],"s_ex":[],"p":[],"p_ex":[]}}
self.atmRecipProjdata [=] {"element",[float(proj_gmax),{"orbtypes":[proj_recip_radial_data]}]}
self.atmPsuedoAeData [=] {"element",[radial_grid, {"orbtypes":[pseudo_radial_data]}}, {"orbtypes":[ae_radial_data]}]} e.g. {"Si,[[0,0.01,...,1.45],{"s":[],"s_ex":[],"p":[],"p_ex":[]},{"s":[],"s_ex":[],"p":[],"p_ex":[]}]</p>
                        </div>
                    </div>

                    <div class="method" id="get_orbs_fromPOT">
                        <div class="method-header">
                            <h4>get_orbs_fromPOT</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1166" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_orbs_fromPOT(self, orbfactor=1.0)</code>
                        </div>

                        <div class="method-description">
                            <p>Creates the 3D initial orbitals in real space from the pseudo radial orbitals.
Also sets the amount of orbitals by looping through atoms and their orbitals, thus intializes many orbital-dependent variables</p>
                        </div>
                    </div>

                    <div class="method" id="get_coefficients">
                        <div class="method-header">
                            <h4>get_coefficients</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1786" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_coefficients(self, orbitalWF, crystalWF, overlap_matrix, recip=False, band=None)</code>
                        </div>

                        <div class="method-description">
                            <p>Find the coefficients for the amount of each pseudo orbital (Φ) in the pseudo wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an</p>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>The coefficients C_an of orbital a in band n</p>
                        </div>
                    </div>

                    <div class="method" id="get_aecoefficients">
                        <div class="method-header">
                            <h4>get_aecoefficients</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1829" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_aecoefficients(self, orbitalWF, crystalWF, aeoverlap_matrix, kpt, recip=False, band=None, full_kpt=False, prints=False, gpnts=None, set_gpnts=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Find the coefficients for the amount of each ae orbital (Φ) in the ae wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an
The orbital-wavefunction overlap is modified from the pseudo overlap using standard PAW methods</p>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>The coefficients C_na of orbital a in band n</p>
                        </div>
                    </div>

                    <div class="method" id="get_ae_overlap_matrix">
                        <div class="method-header">
                            <h4>get_ae_overlap_matrix</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1915" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_ae_overlap_matrix(self, orbitalWF, secondWF=None, secondisarray=False, recip=True, kpt=0)</code>
                        </div>

                        <div class="method-description">
                            <p>Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ</p>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>The overlap matrix S_ab for orbitals a and b</p>
                        </div>
                    </div>

                    <div class="method" id="get_overlap_matrix">
                        <div class="method-header">
                            <h4>get_overlap_matrix</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L1996" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_overlap_matrix(self, orbitalWF, secondWF=None, secondisarray=False, recip=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ</p>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>The overlap matrix S_ab for orbitals a and b</p>
                        </div>
                    </div>

                    <div class="method" id="lowdin_orth">
                        <div class="method-header">
                            <h4>lowdin_orth</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2041" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>lowdin_orth(self, low_orbitals, set_overlap=False, overlap=None, recip=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Orthogonalized the orbital based on the Lowdin scheme.
The new orbitals Ψ are defined by the original orbitals Φ as Ψ_b = conj(S_ab)^(-1/2)*Φ_a</p>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>Lowdin orthogonalized orbitals</p>
                        </div>
                    </div>

                    <div class="method" id="converge_orbs_recip">
                        <div class="method-header">
                            <h4>converge_orbs_recip</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2077" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>converge_orbs_recip(self, num_steps=50)</code>
                        </div>

                        <div class="method-description">
                            <p>Converge to the atomic-like Bloch orbitals which best fit the DFT wavefunction
This procedes by ____
Setting equal to 0 with run the standard direct algorithm where |X_a> = sum_n(c_na |Y_n>)
Where |Y_n> are the set of band (equal to number of orbitals) of the highest projection
creates global variable one_orbitalWF which is referenced in the Bloch to atomic orbital fitting</p>
                        </div>
                    </div>

                    <div class="method" id="fit_to_atomic_orb">
                        <div class="method-header">
                            <h4>fit_to_atomic_orb</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L2985" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>fit_to_atomic_orb(self, plot_orbs=False)</code>
                        </div>
                    </div>

                    <div class="method" id="spher_bessel_trans">
                        <div class="method-header">
                            <h4>spher_bessel_trans</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4082" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>spher_bessel_trans(self, orbital_coeffs, rad_grid_size=500)</code>
                        </div>
                    </div>

                    <div class="method" id="center_real_orbs">
                        <div class="method-header">
                            <h4>center_real_orbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4118" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>center_real_orbs(self, real_orbs, kpt=0, make_real=False)</code>
                        </div>
                    </div>

                    <div class="method" id="recip_to_real">
                        <div class="method-header">
                            <h4>recip_to_real</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4148" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>recip_to_real(self, recip_orbs, kpt=0, make_real=False)</code>
                        </div>
                    </div>

                    <div class="method" id="real_to_recip">
                        <div class="method-header">
                            <h4>real_to_recip</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4182" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>real_to_recip(self, real_orbs, kpt=0)</code>
                        </div>
                    </div>

                    <div class="method" id="get_kdep_recipprojs">
                        <div class="method-header">
                            <h4>get_kdep_recipprojs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4213" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_kdep_recipprojs(self, kpt, full_kpt=False, for_norm=False, gpnts=None, set_gpnts=False)</code>
                        </div>
                    </div>

                    <div class="method" id="get_kdep_reciporbs">
                        <div class="method-header">
                            <h4>get_kdep_reciporbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4316" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_kdep_reciporbs(self, kpt, full_kpt=False, gpnts=None, set_gpnts=False)</code>
                        </div>
                    </div>

                    <div class="method" id="proj_all_kpoints">
                        <div class="method-header">
                            <h4>proj_all_kpoints</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4370" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>proj_all_kpoints(self, max_bandavg=None, calc_nrms=False)</code>
                        </div>
                    </div>

                    <div class="method" id="optimize_band_set">
                        <div class="method-header">
                            <h4>optimize_band_set</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L4587" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>optimize_band_set(self, band_opt=True, orb_opt=True, orb_orth=False)</code>
                        </div>

                        <div class="parameters-section">
                            <h5>Parameters</h5>
                            <table class="parameters-table">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Type</th>
                                        <th>Description</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><code>kpt</code></td>
                                        <td><code>Any</code></td>
                                        <td>disentangle for a certain kpt, if None do all kpts</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>set of band which minimizes the difference between the orbital states left after and the band set orbital states;   maybe later: also minimize overlap between Lowdin orthogonalized band sets outline: start by finding the lowest band with projectibilty < 0.8 keep and lowdin orthogonailze everything beneath that band discard any band with projectibility < 0.2 calculate 1-orbital states over all the good states > 0.8 calculate orbital states of each possible band run through optimization</p>
                        </div>
                    </div>

                    <div class="method" id="expand_irred_kgrid">
                        <div class="method-header">
                            <h4>expand_irred_kgrid</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5019" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>expand_irred_kgrid(self)</code>
                        </div>

                        <div class="method-description">
                            <p>this function does a couple things:
1. finds the kpoints of the reducible grid and the coorespond symmetry operations to get them from the irreducible points
2. creates the eigenvalues, eigenvectors, and overlaps matrices for the new reducible kpoint grid</p>
                        </div>
                    </div>

                    <div class="method" id="symmetrize_orbs">
                        <div class="method-header">
                            <h4>symmetrize_orbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5672" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>symmetrize_orbs(self, recip_orbs)</code>
                        </div>

                        <div class="method-description">
                            <p>This function is to symmetrize the iterated orbitals to decrease orbital mixing by ensuring orbital has s orbital symmetry</p>
                        </div>
                    </div>

                    <div class="method" id="get_Qab">
                        <div class="method-header">
                            <h4>get_Qab</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5941" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_Qab(self)</code>
                        </div>
                    </div>

                    <div class="method" id="get_ae_overlap_info">
                        <div class="method-header">
                            <h4>get_ae_overlap_info</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L5972" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_ae_overlap_info(self, orbs=None, kpt=0, just_ae_overlap=False, recip=False, test=False, full_kpt=False, gpnts=None, set_gpnts=False)</code>
                        </div>
                    </div>

                    <div class="method" id="get_orth_coeffs">
                        <div class="method-header">
                            <h4>get_orth_coeffs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6191" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_orth_coeffs(self, coeff, kpoint=None)</code>
                        </div>
                    </div>

                    <div class="method" id="get_hamiltonian">
                        <div class="method-header">
                            <h4>get_hamiltonian</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6218" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_hamiltonian(self, kpoints=None)</code>
                        </div>
                    </div>

                    <div class="method" id="make_fit_wannier">
                        <div class="method-header">
                            <h4>make_fit_wannier</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L6389" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>make_fit_wannier(self)</code>
                        </div>
                    </div>

                    <div class="method" id="get_TBparameter">
                        <div class="method-header">
                            <h4>get_TBparameter</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7123" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_TBparameter(self, num_trans=5)</code>
                        </div>
                    </div>

                    <div class="method" id="get_interp_ham">
                        <div class="method-header">
                            <h4>get_interp_ham</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7185" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_interp_ham(self, kind, return_truevec=True, return_params=False)</code>
                        </div>
                    </div>

                    <div class="method" id="get_neighbors">
                        <div class="method-header">
                            <h4>get_neighbors</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7225" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_neighbors(self)</code>
                        </div>
                    </div>

                    <div class="method" id="orthogonalize_basis">
                        <div class="method-header">
                            <h4>orthogonalize_basis</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7246" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>orthogonalize_basis(self)</code>
                        </div>
                    </div>

                    <div class="method" id="get_offset">
                        <div class="method-header">
                            <h4>get_offset</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7309" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_offset(self, a=2)</code>
                        </div>
                    </div>

                    <div class="method" id="write_TBfiles">
                        <div class="method-header">
                            <h4>write_TBfiles</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7371" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>write_TBfiles(self)</code>
                        </div>
                    </div>

                    <div class="method" id="write_recip_rad_orbs">
                        <div class="method-header">
                            <h4>write_recip_rad_orbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7428" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>write_recip_rad_orbs(self)</code>
                        </div>
                    </div>

                    <div class="method" id="read_recip_rad_orbs">
                        <div class="method-header">
                            <h4>read_recip_rad_orbs</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7466" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_recip_rad_orbs(self, tag='')</code>
                        </div>
                    </div>

                    <div class="method" id="get_proj_on_aeorb">
                        <div class="method-header">
                            <h4>get_proj_on_aeorb</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7478" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_proj_on_aeorb(self)</code>
                        </div>
                    </div>

                    <div class="method" id="write_input_file">
                        <div class="method-header">
                            <h4>write_input_file</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7521" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>write_input_file(self)</code>
                        </div>
                    </div>

                    <div class="method" id="plot_BS">
                        <div class="method-header">
                            <h4>plot_BS</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7554" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>plot_BS(self)</code>
                        </div>
                    </div>

                    <div class="method" id="plot_projectedBS">
                        <div class="method-header">
                            <h4>plot_projectedBS</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7565" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>plot_projectedBS(self, orbs)</code>
                        </div>
                    </div>

                    <div class="method" id="plot_projectedDOS">
                        <div class="method-header">
                            <h4>plot_projectedDOS</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7600" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>plot_projectedDOS(self, orbs, xlim=None)</code>
                        </div>
                    </div>

                    <div class="method" id="generate_gpnts">
                        <div class="method-header">
                            <h4>generate_gpnts</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7664" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>generate_gpnts(self, kpt)</code>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <div id="functions" class="tab-content">

        <div class="function-section" id="func_for_rad">
            <div class="function-header">
                <h2>func_for_rad</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7714" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>func_for_rad(x, a, b, c, d, e, f, g, h, l)</code>
            </div>
        </div>

        <div class="function-section" id="func_for_rad_fit">
            <div class="function-header">
                <h2>func_for_rad_fit</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7717" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>func_for_rad_fit(x, a, b, con1, con2, con3, c, g, con4, l)</code>
            </div>
        </div>

        <div class="function-section" id="func_for_rad_exp">
            <div class="function-header">
                <h2>func_for_rad_exp</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7725" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>func_for_rad_exp(x, a, b, c, d, e, f, l)</code>
            </div>
        </div>

        <div class="function-section" id="lowdin_orth_vectors">
            <div class="function-header">
                <h2>lowdin_orth_vectors</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7728" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>lowdin_orth_vectors(vectors)</code>
            </div>
        </div>

        <div class="function-section" id="lowdin_orth_vectors_orblap">
            <div class="function-header">
                <h2>lowdin_orth_vectors_orblap</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7754" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>lowdin_orth_vectors_orblap(vectors, orblap, energies=None, return_energy=False)</code>
            </div>
        </div>

        <div class="function-section" id="gs_orth_twoloworthsets">
            <div class="function-header">
                <h2>GS_orth_twoLoworthSets</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7800" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>GS_orth_twoLoworthSets(vectors1, vectors2)</code>
            </div>
        </div>

        <div class="function-section" id="gs_orth_twoloworthsets_orblap">
            <div class="function-header">
                <h2>GS_orth_twoLoworthSets_orblap</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7826" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>GS_orth_twoLoworthSets_orblap(vectors1, vectors2, orblap, energy1=None, energy2=None, return_energy=False, energycut=0, ratio=...)</code>
            </div>
        </div>

        <div class="function-section" id="gs_combine_states_orblap">
            <div class="function-header">
                <h2>GS_combine_states_orblap</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7895" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>GS_combine_states_orblap(vectors1, vectors2, orblap, energy1=None, energy2=None, return_energy=False)</code>
            </div>
        </div>

        <div class="function-section" id="complex128funs">
            <div class="function-header">
                <h2>complex128funs</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7956" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>complex128funs(phi, theta, sphharm_key)</code>
            </div>
        </div>

        <div class="function-section" id="normalize_wf">
            <div class="function-header">
                <h2>normalize_wf</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7979" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>normalize_wf(wavefunc, prim_vec, gridnum, return_integral=False, recip=False)</code>
            </div>
        </div>

        <div class="function-section" id="periodic_integral_3d">
            <div class="function-header">
                <h2>periodic_integral_3d</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L7992" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>periodic_integral_3d(f, prim_vec, n, multiple_wfs=False)</code>
            </div>
        </div>

        <div class="function-section" id="reciprocal_integral">
            <div class="function-header">
                <h2>reciprocal_integral</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8032" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>reciprocal_integral(f)</code>
            </div>
        </div>

        <div class="function-section" id="_cart_to_red">
            <div class="function-header">
                <h2>_cart_to_red</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8045" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>_cart_to_red(tmp, cart)</code>
            </div>

            <div class="function-description">
                <p>Convert cartesian vectors cart to reduced coordinates of a1,a2,a3 vectors</p>
            </div>
        </div>

        <div class="function-section" id="_red_to_cart">
            <div class="function-header">
                <h2>_red_to_cart</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8061" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>_red_to_cart(prim_vec, prim_coord)</code>
            </div>

                        <div class="parameters-section">
                            <h5>Parameters</h5>
                            <table class="parameters-table">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Type</th>
                                        <th>Description</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><code>prim_vec</code></td>
                                        <td><code>Any</code></td>
                                        <td>three float tuples representing the primitive vectors</td>
                                    </tr>
                                    <tr>
                                        <td><code>prim_coord</code></td>
                                        <td><code>Any</code></td>
                                        <td>list of float tuples for primitive coordinates</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

            <div class="returns-section">
                <h4>Returns</h4>
                <p>list of float tuples for cartesian coordinates ex: cart_coord = _red_to_cart((a1,a2,a3),prim_coord)</p>
            </div>
        </div>

        <div class="function-section" id="smooth">
            <div class="function-header">
                <h2>smooth</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8076" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>smooth(y, box_pts)</code>
            </div>
        </div>

        <div class="function-section" id="extract_line_data">
            <div class="function-header">
                <h2>extract_line_data</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8082" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>extract_line_data(grid, gridXYZ, p1, p2, tolerance=0.5)</code>
            </div>

            <div class="function-description">
                <p>Extracts orbital magnitude along a line passing through p1 and p2 in a non-Cartesian 3D grid.
Parameters:
grid (numpy.ndarray): 3D array of orbital magnitudes.
gridXYZ (numpy.ndarray): 2D array (3, num_points) of real-space coordinates.
p1 (tuple): First point (x1, y1, z1) in real space.
p2 (tuple): Second point (x2, y2, z2) in real space.
tolerance (float): Distance threshold to include points near the line.
Returns:
distances (numpy.ndarray): Distances along the line.
magnitudes (numpy.ndarray): Orbital magnitudes at corresponding distances.</p>
            </div>
        </div>

        <div class="function-section" id="combine_and_save_plots">
            <div class="function-header">
                <h2>combine_and_save_plots</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8130" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>combine_and_save_plots(plots, filename='combined_plot.png', layout=None)</code>
            </div>

            <div class="function-description">
                <p>Combines multiple Matplotlib plots into a single figure and saves to a file.
Parameters:
plots (list of matplotlib.figure.Figure): List of Matplotlib figures.
filename (str): Output filename (supports .png, .pdf, .svg, etc.).
layout (tuple or str): (rows, cols) for custom layout or "auto" for automatic grid.
Returns:
None</p>
            </div>
        </div>

        <div class="function-section" id="plot_matrix">
            <div class="function-header">
                <h2>plot_matrix</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITO.py#L8179" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>plot_matrix(matrix, low_center=0.2, high_center=0.85, filename='matrix.png')</code>
            </div>
        </div>
    </div>
</div>

<!-- ReadTheDocs-style CSS -->
<style>
.api-module-header {
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 20px;
    margin-bottom: 30px;
}

.module-description {
    color: #666;
    font-size: 16px;
    margin: 10px 0;
}

.api-tabs {
    margin: 20px 0;
}

.tab-buttons {
    border-bottom: 1px solid #ddd;
    margin-bottom: 20px;
}

.tab-btn {
    background: none;
    border: none;
    padding: 12px 20px;
    cursor: pointer;
    font-size: 14px;
    color: #666;
    border-bottom: 3px solid transparent;
    margin-right: 10px;
    transition: all 0.3s ease;
}

.tab-btn.active {
    color: #2c5aa0;
    border-bottom-color: #2c5aa0;
    font-weight: 600;
}

.tab-btn:hover {
    color: #2c5aa0;
}

.tab-content {
    display: none;
}

.tab-content.active {
    display: block;
}

.class-section, .function-section {
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin-bottom: 30px;
    overflow: hidden;
}

.class-header, .function-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.class-header h2, .function-header h2 {
    margin: 0;
    font-size: 20px;
    color: #2c5aa0;
    font-weight: 600;
}

.class-description, .function-description {
    padding: 20px;
    background: white;
    border-bottom: 1px solid #f0f0f0;
}

.methods-section {
    background: white;
}

.methods-section h3 {
    margin: 0;
    padding: 16px 20px;
    background: #f8f9fa;
    border-bottom: 1px solid #e1e4e8;
    font-size: 16px;
    color: #2c5aa0;
}

.methods-list {
    padding: 0;
}

.method {
    border-bottom: 1px solid #f0f0f0;
    padding: 20px;
}

.method:last-child {
    border-bottom: none;
}

.method-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}

.method-header h4 {
    margin: 0;
    font-size: 16px;
    color: #2c5aa0;
    font-weight: 600;
}

.signature {
    background: #f6f8fa;
    padding: 12px 16px;
    border-radius: 6px;
    border: 1px solid #e1e4e8;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.method-description, .function-description p {
    margin: 12px 0;
    line-height: 1.6;
    color: #333;
}

.parameters-section, .returns-section, .raises-section, .examples-section {
    margin: 16px 0;
}

.parameters-section h5, .returns-section h5, .raises-section h5, .examples-section h5,
.returns-section h4, .examples-section h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.parameters-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 14px;
}

.parameters-table th {
    background: #f6f8fa;
    padding: 12px;
    text-align: left;
    border: 1px solid #e1e4e8;
    font-weight: 600;
    color: #2c5aa0;
    font-size: 13px;
}

.parameters-table td {
    padding: 12px;
    border: 1px solid #e1e4e8;
    vertical-align: top;
}

.parameters-table code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #2c5aa0;
}

.source-link {
    font-size: 12px;
}

.source-link a {
    color: #666;
    text-decoration: none;
    background: #f0f0f0;
    padding: 4px 8px;
    border-radius: 3px;
    transition: all 0.2s ease;
}

.source-link a:hover {
    background: #e0e0e0;
    color: #2c5aa0;
}

.raises-section ul {
    margin: 8px 0;
    padding-left: 20px;
}

.raises-section li {
    margin: 4px 0;
}

.examples-section pre {
    background: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    border: 1px solid #e1e4e8;
    overflow-x: auto;
    margin: 8px 0;
}

.examples-section code {
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    color: #333;
}
</style>

<!-- ReadTheDocs-style JavaScript -->
<script>
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab content
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }

    // Add active class to clicked button
    event.target.classList.add('active');
}

// Initialize first tab as active on page load
document.addEventListener('DOMContentLoaded', function() {
    const firstTabButton = document.querySelector('.tab-btn');
    const firstTabContent = document.querySelector('.tab-content');

    if (firstTabButton && firstTabContent) {
        firstTabButton.classList.add('active');
        firstTabContent.classList.add('active');
    }
});
</script>
