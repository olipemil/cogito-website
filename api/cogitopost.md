---
layout: readthedocs
title: COGITOpost API
module: cogitopost
nav_order: 3
parent: API Documentation
---

<section id="module-COGITOpost">
<span id="cogitopost-module"></span><h1>COGITOpost module<a class="headerlink" href="#module-COGITOpost" title="Link to this heading"></a></h1>
<dl class="py class">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">COGITO_TB_Model</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">file_suffix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbs_orth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin_polar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model" title="Link to this definition"></a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">file_suffix</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbs_orth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin_polar</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.__init__"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.__init__" title="Link to this definition"></a></dt>
<dd><p>Initializes the</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>directory</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – The path for the input files</p></li>
<li><p><strong>verbose</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – How much will be printed (0 is least)</p></li>
<li><p><strong>file_suffix</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – The suffix to the TBparams and overlaps files</p></li>
<li><p><strong>orbs_orth</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether the orbitals are orthogonal, if from COGITO this is always False</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.read_input">
<span class="sig-name descname"><span class="pre">read_input</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'tb_input.txt'</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.read_input"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.read_input" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.read_TBparams">
<span class="sig-name descname"><span class="pre">read_TBparams</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'TBparams.txt'</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.read_TBparams"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.read_TBparams" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.read_overlaps">
<span class="sig-name descname"><span class="pre">read_overlaps</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'overlaps.txt'</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.read_overlaps"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.read_overlaps" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.read_orbitals">
<span class="sig-name descname"><span class="pre">read_orbitals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'orbitals.npy'</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.read_orbitals"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.read_orbitals" title="Link to this definition"></a></dt>
<dd><p>This function reads in the orbitals as coefficents for a gaussian expansion.
The information in ‘orbitals.npy’ is combined with the orbital data in ‘tb_input.txt’.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>file</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Orbital file</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.normalize_params">
<span class="sig-name descname"><span class="pre">normalize_params</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.normalize_params"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.normalize_params" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.set_hoppings">
<span class="sig-name descname"><span class="pre">set_hoppings</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb1</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orb2</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">trans</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.set_hoppings"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.set_hoppings" title="Link to this definition"></a></dt>
<dd><p>Change a TB parameter</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>value</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The new parameter</p></li>
<li><p><strong>orb1</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The first orbital index of the parameter</p></li>
<li><p><strong>orb2</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The second orbital index of the parameter</p></li>
<li><p><strong>trans</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code>) – The tuple of translation indices</p></li>
</ul>
</dd>
<dt class="field-even">Return type<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.restrict_params">
<span class="sig-name descname"><span class="pre">restrict_params</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">maximum_dist</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">12.0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">minimum_value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.0001</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.restrict_params"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.restrict_params" title="Link to this definition"></a></dt>
<dd><p>Generates self.use_tbparams, self.use_overlaps, and self.use_vecs_to_orbs which are used in the gen_ham() funciton
With this, the calculation of hamiltonians by gen_ham() is both sparse and vectorized</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>maximum_dist</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximmum distance between hopping parameters which should be included</p></li>
<li><p><strong>minimum_value</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The minimum magnitude of hopping parameter which should be included</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.make_orbitals">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">make_orbitals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cartXYZ</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.make_orbitals"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.make_orbitals" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.plot_orbitals">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">plot_orbitals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.plot_orbitals"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.plot_orbitals" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.generate_gpnts">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">generate_gpnts</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">int64</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.generate_gpnts"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.generate_gpnts" title="Link to this definition"></a></dt>
<dd><p>similar to from pymatgen.io.vasp.outputs.Wavecar but is vectorized</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>kpt</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – The k-point in reduced coordinates</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The gpoints</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>npt.NDArray[<a href="#id1"><span class="problematic" id="id2">np.int_</span></a>]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_ham">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_ham</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_overlap</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_truevec</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_ham"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_ham" title="Link to this definition"></a></dt>
<dd><p>This function generates the hamiltonian and overlap matrices for a given kpt.
Then it solves the generalized eigenvalue problem to return the eigvalues and vectors</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – An object with the attributes of the COGITO_TB_Model class</p></li>
<li><p><strong>kpt</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – The kpoint to regenerate at in reduced coordinates</p></li>
<li><p><strong>return_overlap</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If True, the function will also return the overlap matrix at the kpt; default is False</p></li>
<li><p><strong>return_truevec</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If True, the function will return the eigenvectors in the original nonorthogonal basis
Default if True</p></li>
<li><p><strong>spin</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The spin of the parameters for a spin-polarized calculation; default is 0–for non spin-polarized</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>returns a list of the eigenvalues and eigenvectors (and overlap if return_overlap=True)</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>list</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_fullHam">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_fullHam</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpt</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_fullHam"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_fullHam" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_neighbors">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_neighbors</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_neighbors"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_neighbors" title="Link to this definition"></a></dt>
<dd><p>This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.plot_crystal_field">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">plot_crystal_field</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atomnum</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbitals</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'d'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">0)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.plot_crystal_field"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.plot_crystal_field" title="Link to this definition"></a></dt>
<dd><p>Plots the crystal field splitting diagram for the orbitals and atom given</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>atomnum</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Which atom to plot for</p></li>
<li><p><strong>orbitals</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Which orbitals to plot, “d” is most common</p></li>
<li><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – The limits of the y-axis in the plot, will default to good value if left (-10,0)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.plot_hopping">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">plot_hopping</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.plot_hopping"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.plot_hopping" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.plot_overlaps">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">plot_overlaps</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.plot_overlaps"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.plot_overlaps" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.compare_to_DFT">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">compare_to_DFT</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">directory</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">extra_tag</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.compare_to_DFT"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.compare_to_DFT" title="Link to this definition"></a></dt>
<dd><p>This function reads the EIGENVAL from a DFT run, generates the energies from the TB model for the kpt grid,
And plots and compares the error between the TB model energies and DFT energies</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – An object of the class COGITO_TB_Model (can not be the BAND or UNIFORM classes!)</p></li>
<li><p><strong>directory</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – The directory where the EIGENVAL file is</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><dl class="simple">
<dt>Returns a list of the (averaged over the valance bands) band distance (as defined by Marzari),</dt><dd><p>average maximum error, and average band error</p>
</dd>
</dl>
</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>list</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_COHP">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_COHP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">_ScalarType_co</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_COHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_COHP" title="Link to this definition"></a></dt>
<dd><p>Calculates the COHP for the given orbitals and nearest neighbors</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – An object of the class COGITO_BAND or COGITO_UNIFORM</p></li>
<li><p><strong>orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</p></li>
<li><p><strong>NN</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors</p></li>
<li><p><strong>include_onsite</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms</p></li>
<li><p><strong>spin</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The spin of the tight binding parameters; default is 0 works for nonspin-polarized</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>returns COHP values in a [kpt,band] dimension</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>npt.NDArray</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_ICOHP">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_ICOHP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">_ScalarType_co</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_ICOHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_ICOHP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_COOP">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_COOP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">_ScalarType_co</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_COOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_COOP" title="Link to this definition"></a></dt>
<dd><p>Calculates the COOP for the given orbitals and nearest neighbors</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – An object of the class COGITO_BAND or COGITO_UNIFORM</p></li>
<li><p><strong>orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</p></li>
<li><p><strong>NN</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors</p></li>
<li><p><strong>include_onsite</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure</p></li>
<li><p><strong>spin</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The spin of the tight binding parameters; default is 0 works for nonspin-polarized</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>returns COOP values in a [kpt,band] dimension</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>npt.NDArray</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_TB_Model.get_ICOOP">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_ICOOP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">_ScalarType_co</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_TB_Model.get_ICOOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_TB_Model.get_ICOOP" title="Link to this definition"></a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">COGITO_BAND</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND" title="Link to this definition"></a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.__init__"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.__init__" title="Link to this definition"></a></dt>
<dd><p>This class deals with all post-processing band structure analysis</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>TB_model</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – requires an object of the class COGITO_TB_Model</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.get_bandstructure">
<span class="sig-name descname"><span class="pre">get_bandstructure</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.get_bandstructure"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.get_bandstructure" title="Link to this definition"></a></dt>
<dd><p>The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>num_kpts</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The number of kpoints between EACH kpath</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.plotBS">
<span class="sig-name descname"><span class="pre">plotBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ax</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">color_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ndarray</span><span class="p"><span class="pre">[</span></span><span class="pre">tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">int</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">dtype</span><span class="p"><span class="pre">[</span></span><span class="pre">_ScalarType_co</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">np.array([])</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">object</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.plotBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.plotBS" title="Link to this definition"></a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ax</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis</p></li>
<li><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Limits on the y-axis of plot</p></li>
<li><p><strong>color_label</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – When being plotted from another function, this passes “COHP” or “COOP”</p></li>
<li><p><strong>colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">npt.NDArray</span></code>) – Magnitude for each point to use in color plotting, passed by get_COHP() function</p></li>
<li><p><strong>colorhalf</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – Sets scale of color bar</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>matplotlib.pyplot axis with bandstructure plotted</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.plotlyBS">
<span class="sig-name descname"><span class="pre">plotlyBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">color_label</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbProj</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">object</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.plotlyBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.plotlyBS" title="Link to this definition"></a></dt>
<dd><p>Plots bandstructure (or projected bandstructure) using plotly graph_objects</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – Limits on the y-axis of plot</p></li>
<li><p><strong>color_label</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – When being plotted from another function, this passes “COHP” or “COOP”</p></li>
<li><p><strong>colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – Magnitude for each point to use in color plotting, passed by get_COHP() function</p></li>
<li><p><strong>colorhalf</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – Sets scale of color bar</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>plotly figure with bandstructure plotted</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.get_COHP">
<span class="sig-name descname"><span class="pre">get_COHP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">from_dash</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.get_COHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.get_COHP" title="Link to this definition"></a></dt>
<dd><p>Calculates and plots the projected COHP values for each band and k-point on band structure</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</p></li>
<li><p><strong>NN</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors</p></li>
<li><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – The limits of the y-axis (energy) of the band structure plot</p></li>
<li><p><strong>colorhalf</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COHP)*3</p></li>
<li><p><strong>include_onsite</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms</p></li>
<li><p><strong>from_dash</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.get_COOP">
<span class="sig-name descname"><span class="pre">get_COOP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">from_dash</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">color_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'COOP'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbProj</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.get_COOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.get_COOP" title="Link to this definition"></a></dt>
<dd><p>Calculates and plots the projected COOP values for each band and k-point on band structure</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>orbs</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code>) – either a list of two dictionaries giving elements as keys and orbital types as items (eg [{“Pb”:[“s”,”d”],”O”:[“s”,”p”]},{“Pb”:[“s”]”O”:[“p”]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</p></li>
<li><p><strong>NN</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or “All” for all nearest neighbors</p></li>
<li><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – The limits of the y-axis (energy) of the band structure plot</p></li>
<li><p><strong>colorhalf</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – Set the magnitude for the color bar; For default value of 10, it is set automatically to average(COOP)*3</p></li>
<li><p><strong>include_onsite</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Includes atomic overlap terms (S_ab(R) where R=0 and a=b) instead of just bonding terms, this can be used with NN=0 to give a projected bandstructure</p></li>
<li><p><strong>from_dash</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – Flag to set when calling from the dash app, sets plotting backend to plotly and returns the axis</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.get_projectedBS">
<span class="sig-name descname"><span class="pre">get_projectedBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbdict</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.get_projectedBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.get_projectedBS" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BAND.make_COHP_dashapp">
<span class="sig-name descname"><span class="pre">make_COHP_dashapp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">pathname</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'/COGITO_COHP/'</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BAND.make_COHP_dashapp"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BAND.make_COHP_dashapp" title="Link to this definition"></a></dt>
<dd><p>This function generate a dash app which allows the user to interactively select orbitals and nearest neighbors
to examine their project COHP band structure quickly</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pathname</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Name appended to the default pathname for the html</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">COGITO_UNIFORM</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM" title="Link to this definition"></a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.__init__"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.__init__" title="Link to this definition"></a></dt>
<dd><p>This class deals with all post-processing uniform grid analysis</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>TB_model</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – requires an object of the class COGITO_TB_Model</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_uniform">
<span class="sig-name descname"><span class="pre">get_uniform</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">grid</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">tuple</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_uniform"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_uniform" title="Link to this definition"></a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>grid</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code>) – The kpoint grid to use for the uniform sampling</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.recalc_efermi">
<span class="sig-name descname"><span class="pre">recalc_efermi</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.recalc_efermi"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.recalc_efermi" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_occupation">
<span class="sig-name descname"><span class="pre">get_occupation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">spin</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_occupation"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_occupation" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_COHP">
<span class="sig-name descname"><span class="pre">get_COHP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">sigma</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_COHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_COHP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_ICOHP">
<span class="sig-name descname"><span class="pre">get_ICOHP</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_ICOHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_ICOHP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.save_ICOHP">
<span class="sig-name descname"><span class="pre">save_ICOHP</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.save_ICOHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.save_ICOHP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_COOP">
<span class="sig-name descname"><span class="pre">get_COOP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">orbs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">NN</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">sigma</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">include_onsite</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbProj</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_COOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_COOP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_projectedDOS">
<span class="sig-name descname"><span class="pre">get_projectedDOS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">elem</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">sigma</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">colorhalf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_projectedDOS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_projectedDOS" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_ICOOP">
<span class="sig-name descname"><span class="pre">get_ICOOP</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_ICOOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_ICOOP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.save_ICOOP">
<span class="sig-name descname"><span class="pre">save_ICOOP</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.save_ICOOP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.save_ICOOP" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.make_bond">
<span class="sig-name descname"><span class="pre">make_bond</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">atmind1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atmind2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">center1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">center2</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">orbCOOP</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cartXYZ</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.make_bond"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.make_bond" title="Link to this definition"></a></dt>
<dd><p>This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>atmind1</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The atom number for the first atom</p></li>
<li><p><strong>atmind2</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The atom number for the second atom</p></li>
<li><p><strong>center1</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The center of the first atom (not using self.primATOMs)</p></li>
<li><p><strong>center2</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The center of the second atom (not using self.primATOMs)</p></li>
<li><p><strong>orbCOOP</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The orbCOOP which reveals how much of each orbital combo that is included in the bond.
Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.</p></li>
<li><p><strong>cartXYZ</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – The 3D flattened grid that the bond density is calculated on</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A 1D array  (3D flattened) of the bond density</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_bonds_figure_old">
<span class="sig-name descname"><span class="pre">get_bonds_figure_old</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">energy_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">offset</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">one_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">bond_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_bonds_figure_old"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_bonds_figure_old" title="Link to this definition"></a></dt>
<dd><p>this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>energy_cutoff</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – This is the minimum bond magnitude that will be plotted</p></li>
<li><p><strong>offset</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The offset in the colors, set different values to try out different colors</p></li>
<li><p><strong>plot_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot</p></li>
<li><p><strong>one_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether only the atom defined in plot_atom should be plotted; default is False</p></li>
<li><p><strong>bond_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximum bond distance that will be plotted outside the primitive cell</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_bonds_figure">
<span class="sig-name descname"><span class="pre">get_bonds_figure</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">energy_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">bond_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3.0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">elem_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">one_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">fovy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_fig</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">only_prim_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_bonds_figure"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_bonds_figure" title="Link to this definition"></a></dt>
<dd><p>this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>energy_cutoff</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – This is the minimum bond magnitude that will be plotted</p></li>
<li><p><strong>bond_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximum bond distance that will be plotted outside the primitive cell</p></li>
<li><p><strong>elem_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the elements based on order in tb_input. Length of list should be the number of
unique elements. Can either be integer list to reference the default colors or list of
plotly compatable colors.</p></li>
<li><p><strong>atom_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the atoms based on order in tb_input. Length of list should be the number of
atoms in the primitive cell. Can either be integer list to reference the default colors or
list of plotly compatable colors. If not set defaults to elem_colors.</p></li>
<li><p><strong>atom_labels</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – List of atom labels as a string.</p></li>
<li><p><strong>plot_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot</p></li>
<li><p><strong>one_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether only the atom defined in plot_atom should be plotted; default is False</p></li>
<li><p><strong>fovy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
Set between 3 (for close to orthographic) and 30 (for good perspective depth).</p></li>
<li><p><strong>return_fig</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object</p></li>
<li><p><strong>only_prim_atoms</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If True, only the atoms within the primitive cell are plotted.
If False, atoms are added outside the primitive cell if the atom has a bond to an atom
inside the primtive cell that meets energy_cutoff and bond_max criteria.
Default is set in code False if self.numAtoms &lt; 30, otherwise set to True</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_bonds_charge_figure">
<span class="sig-name descname"><span class="pre">get_bonds_charge_figure</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">energy_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">bond_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3.0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">elem_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">one_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">fovy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_fig</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">only_prim_atoms</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_bonds_charge_figure"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_bonds_charge_figure" title="Link to this definition"></a></dt>
<dd><p>Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>energy_cutoff</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – This is the minimum bond magnitude that will be plotted</p></li>
<li><p><strong>bond_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximum bond distance that will be plotted outside the primitive cell</p></li>
<li><p><strong>elem_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the elements based on order in tb_input. Length of list should be the number of
unique elements. Can either be integer list to reference the default colors or list of
plotly compatable colors.</p></li>
<li><p><strong>atom_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the atoms based on order in tb_input. Length of list should be the number of
atoms in the primitive cell. Can either be integer list to reference the default colors or
list of plotly compatable colors. If not set defaults to elem_colors.</p></li>
<li><p><strong>atom_labels</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – List of atom labels as a string.</p></li>
<li><p><strong>auto_label</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Different options for plotting includes: (can include multiple in the string)
“mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
“full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
“color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
“color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
NOTE: Only use “mulliken” OR “full”, NOT both</p></li>
<li><p><strong>plot_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot</p></li>
<li><p><strong>one_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether only the atom defined in plot_atom should be plotted; default is False</p></li>
<li><p><strong>fovy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
Set between 3 (for close to orthographic) and 30 (for good perspective depth).</p></li>
<li><p><strong>return_fig</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object</p></li>
<li><p><strong>only_prim_atoms</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – If True, only the atoms within the primitive cell are plotted.
If False, atoms are added outside the primitive cell if the atom has a bond to an atom
inside the primtive cell that meets energy_cutoff and bond_max criteria.
Default is set in code False if self.numAtoms &lt; 30, otherwise set to True</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Depend on return_fig parameter.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_bond_density_figure">
<span class="sig-name descname"><span class="pre">get_bond_density_figure</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">energy_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">iso_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.03</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">iso_min</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">-0.003</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">elem_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_colors</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">atom_labels</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">list</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plot_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">one_atom</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">bond_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3.0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">fovy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_fig</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_bond_density_figure"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_bond_density_figure" title="Link to this definition"></a></dt>
<dd><p>Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>energy_cutoff</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – This is the minimum bond magnitude that will be plotted</p></li>
<li><p><strong>iso_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The positive isosurface for plotting the bonds.</p></li>
<li><p><strong>iso_min</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The negative isosurface for plotting the bonds.</p></li>
<li><p><strong>elem_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the elements based on order in tb_input. Length of list should be the number of
unique elements. Can either be integer list to reference the default colors or list of
plotly compatable colors.</p></li>
<li><p><strong>atom_colors</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – Colors for the atoms based on order in tb_input. Length of list should be the number of
atoms in the primitive cell. Can either be integer list to reference the default colors or
list of plotly compatable colors. If not set defaults to elem_colors.</p></li>
<li><p><strong>atom_labels</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code>) – List of atom labels as a string.</p></li>
<li><p><strong>auto_label</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Different options for plotting includes: (can include multiple in the string)
“mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
“full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
“color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
“color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
NOTE: Only use “mulliken” OR “full”, NOT both</p></li>
<li><p><strong>plot_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – Set with one_atom=True, plots only one atom and it’s bonds, this passes the atom number to plot</p></li>
<li><p><strong>one_atom</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code>) – Whether only the atom defined in plot_atom should be plotted; default is False</p></li>
<li><p><strong>bond_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximum bond distance that will be plotted outside the primitive cell</p></li>
<li><p><strong>fovy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.
Set between 3 (for close to orthographic) and 30 (for good perspective depth).</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing, but saves plotly figure to ‘crystal_bonds.html’</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_bond_info">
<span class="sig-name descname"><span class="pre">get_bond_info</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_bond_info"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_bond_info" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_COHP_DOS_bybond">
<span class="sig-name descname"><span class="pre">get_COHP_DOS_bybond</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sigma</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">return_fig</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_COHP_DOS_bybond"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_COHP_DOS_bybond" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_crystal_plus_COHP">
<span class="sig-name descname"><span class="pre">get_crystal_plus_COHP</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">energy_cutoff</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0.05</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">bond_max</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">3</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_label</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">'mulliken'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">fovy</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">10</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_crystal_plus_COHP"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_crystal_plus_COHP" title="Link to this definition"></a></dt>
<dd><p>The will plot the crystal bond plot on the left with interactivity to a COHP DOS plot on the right</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>energy_cutoff</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – This is the minimum bond magnitude that will be plotted</p></li>
<li><p><strong>bond_max</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – The maximum bond distance that will be plotted outside the primitive cell</p></li>
<li><p><strong>auto_label</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code>) – Different options for plotting includes: (can include multiple in the string)
“mulliken” - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels)
“full” - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels)
“color” - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors)
“color mag” - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors)
NOTE: Only use “mulliken” OR “full”, NOT both</p></li>
<li><p><strong>fovy</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code>) – field of view in the vertical direction. Use this tag to adjust depth perception in crystal.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing, but saved to ‘bond_cohp_plot.html’</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_UNIFORM.get_mulliken_charge">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_mulliken_charge</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">self</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">elem</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_UNIFORM.get_mulliken_charge"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_UNIFORM.get_mulliken_charge" title="Link to this definition"></a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">COGITO_BS_widget</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget" title="Link to this definition"></a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">TB_model</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">object</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.__init__"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.__init__" title="Link to this definition"></a></dt>
<dd><p>This class deals with all post-processing band structure analysis</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>TB_model</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code>) – requires an object of the class COGITO_TB_Model</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.get_bandstructure">
<span class="sig-name descname"><span class="pre">get_bandstructure</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">num_kpts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">100</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.get_bandstructure"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.get_bandstructure" title="Link to this definition"></a></dt>
<dd><p>The function automatically generates a kpath using pymatgen and kpathseek
Then calculates the band energies and vectors for the kpath</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>num_kpts</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code>) – The number of kpoints between EACH kpath</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Nothing</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.plotlyBS">
<span class="sig-name descname"><span class="pre">plotlyBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(-10,</span> <span class="pre">10)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">selectedDot</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plotnew</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">object</span></span></span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.plotlyBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.plotlyBS" title="Link to this definition"></a></dt>
<dd><p>Plots bandstructure (or projected bandstructure) using plotly graph_objects</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ylim</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – Limits on the y-axis of plot</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>plotly figure with bandstructure plotted</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.plotBS">
<span class="sig-name descname"><span class="pre">plotBS</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">selectedDot</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">plotnew</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.plotBS"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.plotBS" title="Link to this definition"></a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ax</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – (matplotlib.pyplot axis): axis to save the bandstructure to, otherwise generate new axis</p></li>
<li><p><strong>selectedDot</strong> (<code class="xref py py-class docutils literal notranslate"><span class="pre">unknown</span></code>) – (1D integer array): gives kpoint and band index of the dot selected to make green circle
eg: [3,4]</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>matplotlib.pyplot axis with bandstructure plotted</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>unknown</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.get_significant_bonds">
<span class="sig-name descname"><span class="pre">get_significant_bonds</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">band</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">kpoint</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">spin</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.get_significant_bonds"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.get_significant_bonds" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.plot_bond_run">
<span class="sig-name descname"><span class="pre">plot_bond_run</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">num_bond</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.plot_bond_run"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.plot_bond_run" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.change_sig_bonds">
<span class="sig-name descname"><span class="pre">change_sig_bonds</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">old_vals</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">new_vals</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tbvals</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_bond</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.change_sig_bonds"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.change_sig_bonds" title="Link to this definition"></a></dt>
<dd><p>To change tight-binding parameter, need to know two orbitals and three translations</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="COGITOpost.COGITO_BS_widget.make_BS_widget">
<span class="sig-name descname"><span class="pre">make_BS_widget</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">app</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#COGITO_BS_widget.make_BS_widget"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.COGITO_BS_widget.make_BS_widget" title="Link to this definition"></a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITOpost.func_for_rad">
<span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">func_for_rad</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">a</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">b</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">c</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">d</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">e</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">f</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">g</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">h</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">l</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#func_for_rad"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.func_for_rad" title="Link to this definition"></a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="COGITOpost.complex128funs">
<span class="sig-prename descclassname"><span class="pre">COGITOpost.</span></span><span class="sig-name descname"><span class="pre">complex128funs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">phi</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">theta</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">sphharm_key</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="https://github.com/olipemil/cogito-website/blob/main/COGITO_sample/COGITOpost.py#complex128funs"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#COGITOpost.complex128funs" title="Link to this definition"></a></dt>
<dd></dd></dl>

</section>
