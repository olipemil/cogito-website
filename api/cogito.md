---
layout: readthedocs
title: COGITO Core API
module: cogito
nav_order: 2
parent: API Documentation
---

<section id="module-COGITO">
<span id="cogito-module"></span><h1>COGITO module<a class="headerlink" href="#module-COGITO" title="Link to this heading"></a></h1>
<dl class="py class">
<dt class="sig sig-object py" id="COGITO.COGITO">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">COGITO</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">wavecar_dir</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">readmode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO" title="Link to this definition"></a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">wavecar_dir</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">readmode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin_polar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.__init__"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.__init__" title="Link to this definition"></a></dt>
<dd><p>intialize the calculation</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>wavecar_dir</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – The directory with all the VASP output files</p></li>
<li><p><strong>readmode</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If true, the code should have been run with readmode=False to generate output files;
will not read VASP output files or run orbital convergence and projection</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.generate_TBmodel">
<span class="sig-name descname"><span class="pre">generate_TBmodel</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">irreducible_grid</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_excited</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">save_orb_data</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">save_orb_figs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_orbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_projBS</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_projDOS</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">calc_nrms</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbfactor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_steps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">50</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_outer</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tag</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">min_proj</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.02</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">band_opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb_opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb_orth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">start_from_orbnpy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">minimum_orb_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-60</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">min_duplicate_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-60</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.generate_TBmodel"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.generate_TBmodel" title="Link to this definition"></a></dt>
<dd><p>Runs all the functions neccessary to generate the TB interpolation.
REQUIRES UNIFORM KPT GRID WITH NO SYMMETRY OR FULL SYMMETRY FOR TB MODEL</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>irreducible_grid</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether or not the kpoint grid is irreducible. True for ISYM=1|2|3; False for ISYM=-1 (does not work with ISYM=0)</p></li>
<li><p><strong>verbose</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – how much to ouput, includes 0,1,2,3. Higher numbers result in more output</p></li>
<li><p><strong>include_excited</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – how much to include excited orbital states, includes 0, 1, 2. To do this best avoid using POTCARs with semi-core states.
0 includes no excited orbital states (only ones which are partially occupied in isolated atom)
1 includes some excited states (if the POTCAR has the excited states + another higher one of the same l) (generally includes p orbital for d block)
2 includes maximally recommended states (condition of 1 + if the energy listed is the same as in isolated atom) (generally includes p orbitals for 1&amp;2nd row)</p></li>
<li><p><strong>plot_orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Plot the radial converged orbital being fit to Gaussian functions</p></li>
<li><p><strong>plot_projBS</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Plot the orbital projected bandstructure (not BS if the kpt grid is uniform)</p></li>
<li><p><strong>plot_projDOS</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Plot the orbital projected density of states (not correct DOS unless kpt grid is uniform)</p></li>
<li><p><strong>orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dictionary</span></code>) – The orbitals to plot the projection of. Defaults to all orbitals.
FORMAT: {“element1”:[orbital types]} e.g. {“Si”:[“s”,”p”],”C”:[“s”,”p”]}</p></li>
<li><p><strong>minimum_orb_energy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The lower limit to add semi-core states in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.</p></li>
<li><p><strong>min_duplicate_energy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The lower limit to add semi-core states when there is another valence state of the same l quantum number in the POTCAR into the COGITO basis. Uses the atomic orbital energy listed in POTCAR.</p></li>
</ul>
</dd>
</dl>
<dl class="simple">
<dt>Usage:</dt><dd><p>new_model = COGITO(“silicon/”)
new_model.generate_TBmodel(plot_orbs=True)</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.test_initialorbs">
<span class="sig-name descname"><span class="pre">test_initialorbs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_orbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_excited</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">low_factor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.8</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">high_factor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_fac</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">9</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_outer</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tag</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">min_proj</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.02</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_steps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">50</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">minimum_orb_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-60</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">min_duplicate_energy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-60</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.test_initialorbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.test_initialorbs" title="Link to this definition"></a></dt>
<dd><p>Tests dependance of orbital radius and quality on the size of initial orbitals.
Only runs the convergence of the orbitals without projecting them or generating the TB model</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>verbose</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – how much to ouput, includes 0,1,2,3. Higher numbers result in more output</p></li>
<li><p><strong>plot_orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Plot the radial converged orbital being fit to Gaussian functions</p></li>
<li><p><strong>low_factor</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – minimum to multiply the orbital size by; Default is 80%</p></li>
<li><p><strong>high_factor</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – maximum to multiply the orbital size by; Default is 120%</p></li>
<li><p><strong>num_fac</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – the number of steps between low_factor and high_factor to try</p></li>
</ul>
</dd>
</dl>
<dl class="simple">
<dt>Usage:</dt><dd><p>new_model = COGITO(“silicon/”)
new_model.generate_TBmodel(plot_orbs=True)</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_WFdata_fromPOT">
<span class="sig-name descname"><span class="pre">get_WFdata_fromPOT</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_WFdata_fromPOT"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_WFdata_fromPOT" title="Link to this definition"></a></dt>
<dd><p>Function which reads the pseudo and ae orbital information from the POTCAR
Creates the global variables self.atmProjectordata, self.atmRecipProjdata, and self.atmPsuedoAeData
FORMATs:
self.atmProjectordata [=] {“element”,[float(cutoff_rad),{“orbtypes”:[proj_real_radial_data]}]} e.g. {“Si”,[1.45,{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]}}
self.atmRecipProjdata [=] {“element”,[float(proj_gmax),{“orbtypes”:[proj_recip_radial_data]}]}
self.atmPsuedoAeData [=] {“element”,[radial_grid, {“orbtypes”:[pseudo_radial_data]}}, {“orbtypes”:[ae_radial_data]}]} e.g. {“Si,[[0,0.01,…,1.45],{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]},{“s”:[],”s_ex”:[],”p”:[],”p_ex”:[]}]</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_orbs_fromPOT">
<span class="sig-name descname"><span class="pre">get_orbs_fromPOT</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbfactor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_orbs_fromPOT"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_orbs_fromPOT" title="Link to this definition"></a></dt>
<dd><p>Creates the 3D initial orbitals in real space from the pseudo radial orbitals.
Also sets the amount of orbitals by looping through atoms and their orbitals, thus intializes many orbital-dependent variables</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>orbfactor</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – multipled by the radial part of the pseudo radial orbital to either shrink or grow them</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_coefficients">
<span class="sig-name descname"><span class="pre">get_coefficients</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbitalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">crystalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">overlap_matrix</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">band</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_coefficients"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_coefficients" title="Link to this definition"></a></dt>
<dd><p>Find the coefficients for the amount of each pseudo orbital (Φ) in the pseudo wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbitalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors</p></li>
<li><p><strong>crystalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length N: All the DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF</p></li>
<li><p><strong>overlap_matrix</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">MxM</span></code>) – matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence</p></li>
<li><p><strong>recip</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the wavefunctions are defined in real or reciprocal space</p></li>
<li><p><strong>band</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The coefficients C_an of orbital a in band n</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_aecoefficients">
<span class="sig-name descname"><span class="pre">get_aecoefficients</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbitalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">crystalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">aeoverlap_matrix</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">band</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">full_kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">prints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">set_gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_aecoefficients"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_aecoefficients" title="Link to this definition"></a></dt>
<dd><p>Find the coefficients for the amount of each ae orbital (Φ) in the ae wavefunction (Ψ)
If the overlap is identity, the coefficients would just be the integral of the orbital-wavefunction overlap: Φa*Ψn = O_an
When the overlap is not identity S_ab, obtaining the coefficients (C_bn) requires solving the linear problem S_ab*C_bn = O_an
The orbital-wavefunction overlap is modified from the pseudo overlap using standard PAW methods</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbitalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length M: All the pseudo orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors</p></li>
<li><p><strong>crystalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length N: All the pseudo DFT wavefunctions in a dictionary. The wavefunction is defined on the same space as orbitalWF</p></li>
<li><p><strong>aeoverlap_matrix</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">MxM</span></code>) – matrix of complex float: The overlap of the ae orbitals. NOTE: The orbitals and their overlaps have a k-dependence</p></li>
<li><p><strong>recip</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the wavefunctions are defined in real or reciprocal space</p></li>
<li><p><strong>band</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – If the coefficents of only one band in the crystalWF dict is needed, pass that band as an integer here.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The coefficients C_na of orbital a in band n</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_ae_overlap_matrix">
<span class="sig-name descname"><span class="pre">get_ae_overlap_matrix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbitalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">secondWF</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">secondisarray</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_ae_overlap_matrix"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_ae_overlap_matrix" title="Link to this definition"></a></dt>
<dd><p>Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbitalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors</p></li>
<li><p><strong>secondWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF</p></li>
<li><p><strong>recip</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the orbitals are defined in real or reciprocal space</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The overlap matrix S_ab for orbitals a and b</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_overlap_matrix">
<span class="sig-name descname"><span class="pre">get_overlap_matrix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbitalWF</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">secondWF</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">secondisarray</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_overlap_matrix"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_overlap_matrix" title="Link to this definition"></a></dt>
<dd><p>Finds the overlap matrix S_ab = Φa*φb. If secondWF is not defined, φ = Φ</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbitalWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors</p></li>
<li><p><strong>secondWF</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length N: The second orbital functions in a dictionary. Defined on the same space as orbitalWF</p></li>
<li><p><strong>recip</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the orbitals are defined in real or reciprocal space</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The overlap matrix S_ab for orbitals a and b</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.lowdin_orth">
<span class="sig-name descname"><span class="pre">lowdin_orth</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">low_orbitals</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">set_overlap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">overlap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.lowdin_orth"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.lowdin_orth" title="Link to this definition"></a></dt>
<dd><p>Orthogonalized the orbital based on the Lowdin scheme.
The new orbitals Ψ are defined by the original orbitals Φ as Ψ_b = conj(S_ab)^(-1/2)*Φ_a</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>low_orbitals</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – of length M: All the orbital functions in a dictionary. The orbital may be defined in real 3D space on reciprocal G vectors</p></li>
<li><p><strong>set_overlap</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the orbital overlap is being passed to the function (True) or should be calculated (False)</p></li>
<li><p><strong>overlap</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">MxM</span></code>) – matrix of complex float: The overlap of the orbitals. NOTE: The orbitals and their overlaps have a k-dependence</p></li>
<li><p><strong>recip</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the orbitals are defined in real or reciprocal space</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Lowdin orthogonalized orbitals</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.converge_orbs_recip">
<span class="sig-name descname"><span class="pre">converge_orbs_recip</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">num_steps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">50</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.converge_orbs_recip"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.converge_orbs_recip" title="Link to this definition"></a></dt>
<dd><p>Converge to the atomic-like Bloch orbitals which best fit the DFT wavefunction
This procedes by ____</p>
<p>creates global variable one_orbitalWF which is referenced in the Bloch to atomic orbital fitting</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>num_steps</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Maximum number of steps to perform the convergence;
Setting equal to 0 with run the standard direct algorithm where <a href="#id1"><span class="problematic" id="id2">|</span></a>X_a&gt; = sum_n(c_na <a href="#id3"><span class="problematic" id="id4">|</span></a>Y_n&gt;)
Where <a href="#id5"><span class="problematic" id="id6">|</span></a>Y_n&gt; are the set of band (equal to number of orbitals) of the highest projection</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.fit_to_atomic_orb">
<span class="sig-name descname"><span class="pre">fit_to_atomic_orb</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">plot_orbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.fit_to_atomic_orb"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.fit_to_atomic_orb" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.spher_bessel_trans">
<span class="sig-name descname"><span class="pre">spher_bessel_trans</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbital_coeffs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">rad_grid_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">500</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.spher_bessel_trans"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.spher_bessel_trans" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.center_real_orbs">
<span class="sig-name descname"><span class="pre">center_real_orbs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">real_orbs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">make_real</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.center_real_orbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.center_real_orbs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.recip_to_real">
<span class="sig-name descname"><span class="pre">recip_to_real</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">recip_orbs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">make_real</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.recip_to_real"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.recip_to_real" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.real_to_recip">
<span class="sig-name descname"><span class="pre">real_to_recip</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">real_orbs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.real_to_recip"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.real_to_recip" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_kdep_recipprojs">
<span class="sig-name descname"><span class="pre">get_kdep_recipprojs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">kpt</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">full_kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">for_norm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">set_gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_kdep_recipprojs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_kdep_recipprojs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_kdep_reciporbs">
<span class="sig-name descname"><span class="pre">get_kdep_reciporbs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">kpt</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">full_kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">set_gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_kdep_reciporbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_kdep_reciporbs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.proj_all_kpoints">
<span class="sig-name descname"><span class="pre">proj_all_kpoints</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">max_bandavg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">calc_nrms</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.proj_all_kpoints"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.proj_all_kpoints" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.optimize_band_set">
<span class="sig-name descname"><span class="pre">optimize_band_set</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">band_opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb_opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb_orth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.optimize_band_set"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.optimize_band_set" title="Link to this definition"></a></dt>
<dd><p>outline:
start by finding the lowest band with projectibilty &lt; 0.8
keep and lowdin orthogonailze everything beneath that band
discard any band with projectibility &lt; 0.2
calculate 1-orbital states over all the good states &gt; 0.8
calculate orbital states of each possible band
run through optimization</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>set of band which minimizes the difference between the orbital states left after and the band set orbital states;   maybe later: also minimize overlap between Lowdin orthogonalized band sets</p>
</dd>
<dt class="field-even">Return type<span class="colon">:</span></dt>
<dd class="field-even"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.expand_irred_kgrid">
<span class="sig-name descname"><span class="pre">expand_irred_kgrid</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.expand_irred_kgrid"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.expand_irred_kgrid" title="Link to this definition"></a></dt>
<dd><p>this function does a couple things:
1. finds the kpoints of the reducible grid and the coorespond symmetry operations to get them from the irreducible points
2. creates the eigenvalues, eigenvectors, and overlaps matrices for the new reducible kpoint grid</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.symmetrize_orbs">
<span class="sig-name descname"><span class="pre">symmetrize_orbs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">recip_orbs</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.symmetrize_orbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.symmetrize_orbs" title="Link to this definition"></a></dt>
<dd><p>This function is to symmetrize the iterated orbitals to decrease orbital mixing by ensuring orbital has s orbital symmetry</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_Qab">
<span class="sig-name descname"><span class="pre">get_Qab</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_Qab"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_Qab" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_ae_overlap_info">
<span class="sig-name descname"><span class="pre">get_ae_overlap_info</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">just_ae_overlap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">test</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">full_kpt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">set_gpnts</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_ae_overlap_info"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_ae_overlap_info" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_orth_coeffs">
<span class="sig-name descname"><span class="pre">get_orth_coeffs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">coeff</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpoint</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_orth_coeffs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_orth_coeffs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_hamiltonian">
<span class="sig-name descname"><span class="pre">get_hamiltonian</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">kpoints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_hamiltonian"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_hamiltonian" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.make_fit_wannier">
<span class="sig-name descname"><span class="pre">make_fit_wannier</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.make_fit_wannier"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.make_fit_wannier" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_TBparameter">
<span class="sig-name descname"><span class="pre">get_TBparameter</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">num_trans</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_TBparameter"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_TBparameter" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_interp_ham">
<span class="sig-name descname"><span class="pre">get_interp_ham</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">kind</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_truevec</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_params</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_interp_ham"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_interp_ham" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_neighbors">
<span class="sig-name descname"><span class="pre">get_neighbors</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_neighbors"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_neighbors" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.orthogonalize_basis">
<span class="sig-name descname"><span class="pre">orthogonalize_basis</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.orthogonalize_basis"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.orthogonalize_basis" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_offset">
<span class="sig-name descname"><span class="pre">get_offset</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">a</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_offset"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_offset" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.write_TBfiles">
<span class="sig-name descname"><span class="pre">write_TBfiles</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.write_TBfiles"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.write_TBfiles" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.write_recip_rad_orbs">
<span class="sig-name descname"><span class="pre">write_recip_rad_orbs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.write_recip_rad_orbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.write_recip_rad_orbs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.read_recip_rad_orbs">
<span class="sig-name descname"><span class="pre">read_recip_rad_orbs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">tag</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.read_recip_rad_orbs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.read_recip_rad_orbs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.get_proj_on_aeorb">
<span class="sig-name descname"><span class="pre">get_proj_on_aeorb</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.get_proj_on_aeorb"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.get_proj_on_aeorb" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.write_input_file">
<span class="sig-name descname"><span class="pre">write_input_file</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.write_input_file"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.write_input_file" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.plot_BS">
<span class="sig-name descname"><span class="pre">plot_BS</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.plot_BS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.plot_BS" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.plot_projectedBS">
<span class="sig-name descname"><span class="pre">plot_projectedBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.plot_projectedBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.plot_projectedBS" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.plot_projectedDOS">
<span class="sig-name descname"><span class="pre">plot_projectedDOS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.plot_projectedDOS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.plot_projectedDOS" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITO.COGITO.generate_gpnts">
<span class="sig-name descname"><span class="pre">generate_gpnts</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">kpt</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#COGITO.generate_gpnts"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.COGITO.generate_gpnts" title="Link to this definition"></a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.func_for_rad">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">func_for_rad</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">a</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">b</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">c</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">d</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">e</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">f</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">g</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">h</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">l</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#func_for_rad"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.func_for_rad" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.func_for_rad_fit">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">func_for_rad_fit</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">a</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">b</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">con1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">con2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">con3</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">c</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">g</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">con4</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">l</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#func_for_rad_fit"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.func_for_rad_fit" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.func_for_rad_exp">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">func_for_rad_exp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">a</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">b</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">c</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">d</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">e</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">f</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">l</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#func_for_rad_exp"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.func_for_rad_exp" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.lowdin_orth_vectors">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">lowdin_orth_vectors</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">vectors</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#lowdin_orth_vectors"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.lowdin_orth_vectors" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.lowdin_orth_vectors_orblap">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">lowdin_orth_vectors_orblap</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">vectors</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orblap</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energies</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_energy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#lowdin_orth_vectors_orblap"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.lowdin_orth_vectors_orblap" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.GS_orth_twoLoworthSets">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">GS_orth_twoLoworthSets</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">vectors1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">vectors2</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#GS_orth_twoLoworthSets"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.GS_orth_twoLoworthSets" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.GS_orth_twoLoworthSets_orblap">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">GS_orth_twoLoworthSets_orblap</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">vectors1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">vectors2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orblap</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energy1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energy2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_energy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energycut</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ratio</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#GS_orth_twoLoworthSets_orblap"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.GS_orth_twoLoworthSets_orblap" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.GS_combine_states_orblap">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">GS_combine_states_orblap</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">vectors1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">vectors2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orblap</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energy1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">energy2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_energy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#GS_combine_states_orblap"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.GS_combine_states_orblap" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.complex128funs">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">complex128funs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">phi</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">theta</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">sphharm_key</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#complex128funs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.complex128funs" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.normalize_wf">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">normalize_wf</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">wavefunc</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">prim_vec</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gridnum</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_integral</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recip</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#normalize_wf"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.normalize_wf" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.periodic_integral_3d">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">periodic_integral_3d</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">f</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">prim_vec</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">n</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">multiple_wfs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#periodic_integral_3d"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.periodic_integral_3d" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.reciprocal_integral">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">reciprocal_integral</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">f</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#reciprocal_integral"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.reciprocal_integral" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.smooth">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">smooth</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">y</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">box_pts</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#smooth"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.smooth" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.extract_line_data">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">extract_line_data</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">grid</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">gridXYZ</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">p1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">p2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tolerance</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.5</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#extract_line_data"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.extract_line_data" title="Link to this definition"></a></dt>
<dd><p>Extracts orbital magnitude along a line passing through p1 and p2 in a non-Cartesian 3D grid.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>grid</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) – 3D array of orbital magnitudes.</p></li>
<li><p><strong>gridXYZ</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) – 2D array (3, num_points) of real-space coordinates.</p></li>
<li><p><strong>p1</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code>) – First point (x1, y1, z1) in real space.</p></li>
<li><p><strong>p2</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code>) – Second point (x2, y2, z2) in real space.</p></li>
<li><p><strong>tolerance</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – Distance threshold to include points near the line.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>distances (numpy.ndarray): Distances along the line.
magnitudes (numpy.ndarray): Orbital magnitudes at corresponding distances.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>s</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.combine_and_save_plots">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">combine_and_save_plots</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">plots</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'combined_plot.png'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">layout</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#combine_and_save_plots"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.combine_and_save_plots" title="Link to this definition"></a></dt>
<dd><p>Combines multiple Matplotlib plots into a single figure and saves to a file.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>plots</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span> <span class="pre">of</span> <span class="pre">matplotlib.figure.Figure</span></code>) – List of Matplotlib figures.</p></li>
<li><p><strong>filename</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Output filename (supports .png, .pdf, .svg, etc.).</p></li>
<li><p><strong>layout</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span> <span class="pre">or</span> <span class="pre">str</span></code>) – (rows, cols) for custom layout or “auto” for automatic grid.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>s</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITO.plot_matrix">
<span class="sig-prename descclassname"><span class="pre">COGITO.</span></span><span class="sig-name descname"><span class="pre">plot_matrix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">matrix</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">low_center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">high_center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.85</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'matrix.png'</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITO.py#plot_matrix"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITO.plot_matrix" title="Link to this definition"></a></dt>
<dd></dd></dl>

</section>