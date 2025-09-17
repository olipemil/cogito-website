---
layout: default
title: COGITOico API Reference
nav_order: 2
parent: API Documentation
---

# COGITOico API Reference

<div class="api-module-header">
    <p class="module-description">API reference for the COGITOico module</p>
    <div class="source-link">
        <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py" target="_blank">View Source</a>
    </div>
</div>

<div class="api-tabs">
    <div class="tab-buttons">
        <button class="tab-btn active" onclick="showTab('classes')">Classes</button>
        <button class="tab-btn" onclick="showTab('functions')">Functions</button>
    </div>

    <div id="classes" class="tab-content active">

        <div class="class-section" id="cogito_ico">
            <div class="class-header">
                <h2>class COGITO_ICO</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L12" target="_blank">source</a>
                </div>
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
                                        <td><code>directory</code></td>
                                        <td><code>Any</code></td>
                                        <td>The path for the input files</td>
                                    </tr>
                                    <tr>
                                        <td><code>verbose</code></td>
                                        <td><code>Any</code></td>
                                        <td>How much will be printed (0 is least)</td>
                                    </tr>
                                    <tr>
                                        <td><code>file_suffix</code></td>
                                        <td><code>Any</code></td>
                                        <td>The suffix to the TBparams and overlaps files</td>
                                    </tr>
                                    <tr>
                                        <td><code>orbs_orth</code></td>
                                        <td><code>Any</code></td>
                                        <td>Whether the orbitals are orthogonal, if from COGITO this is always False</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

            <div class="methods-section">
                <h3>Methods</h3>
                <div class="methods-list">

                    <div class="method" id="__init__">
                        <div class="method-header">
                            <h4>__init__</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L13" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>__init__(self, directory, verbose=0, file_suffix='', orbs_orth=False, spin_polar=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Initializes the</p>
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
                                        <td><code>directory</code></td>
                                        <td><code>Any</code></td>
                                        <td>The path for the input files</td>
                                    </tr>
                                    <tr>
                                        <td><code>verbose</code></td>
                                        <td><code>Any</code></td>
                                        <td>How much will be printed (0 is least)</td>
                                    </tr>
                                    <tr>
                                        <td><code>file_suffix</code></td>
                                        <td><code>Any</code></td>
                                        <td>The suffix to the TBparams and overlaps files</td>
                                    </tr>
                                    <tr>
                                        <td><code>orbs_orth</code></td>
                                        <td><code>Any</code></td>
                                        <td>Whether the orbitals are orthogonal, if from COGITO this is always False</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div class="method" id="read_input">
                        <div class="method-header">
                            <h4>read_input</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L76" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_input(self, file='tb_input.txt')</code>
                        </div>
                    </div>

                    <div class="method" id="read_overlaps">
                        <div class="method-header">
                            <h4>read_overlaps</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L158" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_overlaps(self, file='overlaps.txt')</code>
                        </div>
                    </div>

                    <div class="method" id="read_ICOHP">
                        <div class="method-header">
                            <h4>read_ICOHP</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L249" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_ICOHP(self, file='ICOHP.txt')</code>
                        </div>
                    </div>

                    <div class="method" id="read_ICOOP">
                        <div class="method-header">
                            <h4>read_ICOOP</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L373" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_ICOOP(self, file='ICOOP.txt')</code>
                        </div>
                    </div>

                    <div class="method" id="read_orbitals">
                        <div class="method-header">
                            <h4>read_orbitals</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L449" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>read_orbitals(self, file='orbitals.npy')</code>
                        </div>

                        <div class="method-description">
                            <p>This function reads in the orbitals as coefficents for a gaussian expansion.
The information in 'orbitals.npy' is combined with the orbital data in 'tb_input.txt'.</p>
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
                                        <td><code>file</code></td>
                                        <td><code>Any</code></td>
                                        <td>Orbital file</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div class="method" id="save_ICOnpy">
                        <div class="method-header">
                            <h4>save_ICOnpy</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L490" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>save_ICOnpy(self)</code>
                        </div>
                    </div>

                    <div class="method" id="get_neighbors">
                        <div class="method-header">
                            <h4>get_neighbors</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L496" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_neighbors(self)</code>
                        </div>

                        <div class="method-description">
                            <p>This sorts the matrix of TB parameters into terms which are 1NN, 2NN, etc.</p>
                        </div>
                    </div>

                    <div class="method" id="get_bonds_figure">
                        <div class="method-header">
                            <h4>get_bonds_figure</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L514" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_bonds_figure(self, energy_cutoff=0.1, elem_colors=..., atom_colors=..., atom_labels=..., plot_atom=None, one_atom=False, bond_max=3.0, fovy=10, return_fig=False)</code>
                        </div>

                        <div class="method-description">
                            <p>this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p</p>
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
                                        <td><code>energy_cutoff</code></td>
                                        <td><code>Any</code></td>
                                        <td>This is the minimum bond magnitude that will be plotted</td>
                                    </tr>
                                    <tr>
                                        <td><code>elem_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the elements based on order in tb_input. Length of list should be the number of unique elements. Can either be integer list to reference the default colors or list of plotly compatable colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the atoms based on order in tb_input. Length of list should be the number of atoms in the primitive cell. Can either be integer list to reference the default colors or list of plotly compatable colors. If not set defaults to elem_colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_labels</code></td>
                                        <td><code>Any</code></td>
                                        <td>List of atom labels as a string.</td>
                                    </tr>
                                    <tr>
                                        <td><code>plot_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot</td>
                                    </tr>
                                    <tr>
                                        <td><code>one_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Whether only the atom defined in plot_atom should be plotted; default is False</td>
                                    </tr>
                                    <tr>
                                        <td><code>bond_max</code></td>
                                        <td><code>Any</code></td>
                                        <td>The maximum bond distance that will be plotted outside the primitive cell</td>
                                    </tr>
                                    <tr>
                                        <td><code>fovy</code></td>
                                        <td><code>Any</code></td>
                                        <td>field of view in the vertical direction. Use this tag to adjust depth perception in crystal. Set between 3 (for close to orthographic) and 30 (for good perspective depth).</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>Nothing</p>
                        </div>
                    </div>

                    <div class="method" id="get_bonds_charge_figure">
                        <div class="method-header">
                            <h4>get_bonds_charge_figure</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L1188" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_bonds_charge_figure(self, energy_cutoff=0.1, bond_max=3.0, elem_colors=..., atom_colors=..., atom_labels=..., auto_label='', plot_atom=None, one_atom=False, fovy=10, return_fig=False, only_prim_atoms=None, atom_dist_from_prim=3.0)</code>
                        </div>

                        <div class="method-description">
                            <p>this will plot the crystal structure atoms with line weighted by iCOHP
each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p</p>
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
                                        <td><code>energy_cutoff</code></td>
                                        <td><code>Any</code></td>
                                        <td>This is the minimum bond magnitude that will be plotted</td>
                                    </tr>
                                    <tr>
                                        <td><code>bond_max</code></td>
                                        <td><code>Any</code></td>
                                        <td>The maximum bond distance that will be plotted outside the primitive cell</td>
                                    </tr>
                                    <tr>
                                        <td><code>elem_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the elements based on order in tb_input. Length of list should be the number of unique elements. Can either be integer list to reference the default colors or list of plotly compatable colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the atoms based on order in tb_input. Length of list should be the number of atoms in the primitive cell. Can either be integer list to reference the default colors or list of plotly compatable colors. If not set defaults to elem_colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_labels</code></td>
                                        <td><code>Any</code></td>
                                        <td>List of atom labels as a string.</td>
                                    </tr>
                                    <tr>
                                        <td><code>auto_labels</code></td>
                                        <td><code>Any</code></td>
                                        <td>Different options for plotting includes: (can include multiple in the string) "mulliken" - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels) "full" - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels) "color" - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors) "color mag" - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors) NOTE: Only use "mulliken" OR "full", NOT both</td>
                                    </tr>
                                    <tr>
                                        <td><code>plot_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot</td>
                                    </tr>
                                    <tr>
                                        <td><code>one_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Whether only the atom defined in plot_atom should be plotted; default is False</td>
                                    </tr>
                                    <tr>
                                        <td><code>fovy</code></td>
                                        <td><code>Any</code></td>
                                        <td>field of view in the vertical direction. Use this tag to adjust depth perception in crystal. Set between 3 (for close to orthographic) and 30 (for good perspective depth).</td>
                                    </tr>
                                    <tr>
                                        <td><code>return_fig</code></td>
                                        <td><code>Any</code></td>
                                        <td>If False, this function saves figure to crystal_bonds.html. If True, this function will return the plotly figure object</td>
                                    </tr>
                                    <tr>
                                        <td><code>only_prim_atoms</code></td>
                                        <td><code>Any</code></td>
                                        <td>If True, only the atoms within the primitive cell are plotted. If False, atoms are added outside the primitive cell if the atom has a bond to an atom inside the primtive cell that meets energy_cutoff and bond_max criteria. Default is set in code False if self.numAtoms < 30, otherwise set to True</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>Depend on return_fig parameter.</p>
                        </div>
                    </div>

                    <div class="method" id="make_bond">
                        <div class="method-header">
                            <h4>make_bond</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L2279" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>make_bond(self, atmind1, atmind2, center1, center2, orbCOOP, cartXYZ)</code>
                        </div>

                        <div class="method-description">
                            <p>This is a function which will generate populate the cartXYZ grid with values for the bond density between
the atoms given using the orbCOOP provided.</p>
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
                                        <td><code>atmind1</code></td>
                                        <td><code>Any</code></td>
                                        <td>The atom number for the first atom</td>
                                    </tr>
                                    <tr>
                                        <td><code>atmind2</code></td>
                                        <td><code>Any</code></td>
                                        <td>The atom number for the second atom</td>
                                    </tr>
                                    <tr>
                                        <td><code>center1</code></td>
                                        <td><code>Any</code></td>
                                        <td>The center of the first atom (not using self.primATOMs)</td>
                                    </tr>
                                    <tr>
                                        <td><code>center2</code></td>
                                        <td><code>Any</code></td>
                                        <td>The center of the second atom (not using self.primATOMs)</td>
                                    </tr>
                                    <tr>
                                        <td><code>orbCOOP</code></td>
                                        <td><code>Any</code></td>
                                        <td>The orbCOOP which reveals how much of each orbital combo that is included in the bond. Dimension nxm where n is the # of orbitals for atom 1 and m is # of orbitals for atom 2.</td>
                                    </tr>
                                    <tr>
                                        <td><code>cartXYZ</code></td>
                                        <td><code>Any</code></td>
                                        <td>The 3D flattened grid that the bond density is calculated on</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>A 1D array  (3D flattened) of the bond density</p>
                        </div>
                    </div>

                    <div class="method" id="get_bond_density_figure">
                        <div class="method-header">
                            <h4>get_bond_density_figure</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L2357" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_bond_density_figure(self, energy_cutoff=0.1, iso_max=0.03, iso_min=0.003, elem_colors=..., atom_colors=..., atom_labels=..., auto_label='', plot_atom=None, one_atom=False, bond_max=3.0, fovy=10, return_fig=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Plots the crystal structure atoms with bonds plotted based on iCOHP
Each line should also be hoverable to reveal the number and amounts that are s-s,s-p, and p-p
The charge and magnetic moment will also be plotted acording to auto_label</p>
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
                                        <td><code>energy_cutoff</code></td>
                                        <td><code>Any</code></td>
                                        <td>This is the minimum bond magnitude that will be plotted</td>
                                    </tr>
                                    <tr>
                                        <td><code>iso_max</code></td>
                                        <td><code>Any</code></td>
                                        <td>The positive isosurface for plotting the bonds.</td>
                                    </tr>
                                    <tr>
                                        <td><code>iso_min</code></td>
                                        <td><code>Any</code></td>
                                        <td>The negative isosurface for plotting the bonds.</td>
                                    </tr>
                                    <tr>
                                        <td><code>elem_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the elements based on order in tb_input. Length of list should be the number of unique elements. Can either be integer list to reference the default colors or list of plotly compatable colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_colors</code></td>
                                        <td><code>Any</code></td>
                                        <td>Colors for the atoms based on order in tb_input. Length of list should be the number of atoms in the primitive cell. Can either be integer list to reference the default colors or list of plotly compatable colors. If not set defaults to elem_colors.</td>
                                    </tr>
                                    <tr>
                                        <td><code>atom_labels</code></td>
                                        <td><code>Any</code></td>
                                        <td>List of atom labels as a string.</td>
                                    </tr>
                                    <tr>
                                        <td><code>auto_label</code></td>
                                        <td><code>Any</code></td>
                                        <td>Different options for plotting includes: (can include multiple in the string) "mulliken" - plots the onsite charge and mag (if spin_polar) on atoms by mulliken population (overrides atom_labels) "full" - plots the charge and magnetics moments (if spin_polar) on atoms and bonds (overrides atom_labels) "color" - colors the atoms and bonds based on their charge (overrides atom_colors or elem_colors) "color mag" - colors the atoms and bonds based on their magnetic moments (overrides atom_colors or elem_colors) NOTE: Only use "mulliken" OR "full", NOT both</td>
                                    </tr>
                                    <tr>
                                        <td><code>plot_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Set with one_atom=True, plots only one atom and it's bonds, this passes the atom number to plot</td>
                                    </tr>
                                    <tr>
                                        <td><code>one_atom</code></td>
                                        <td><code>Any</code></td>
                                        <td>Whether only the atom defined in plot_atom should be plotted; default is False</td>
                                    </tr>
                                    <tr>
                                        <td><code>bond_max</code></td>
                                        <td><code>Any</code></td>
                                        <td>The maximum bond distance that will be plotted outside the primitive cell</td>
                                    </tr>
                                    <tr>
                                        <td><code>fovy</code></td>
                                        <td><code>Any</code></td>
                                        <td>field of view in the vertical direction. Use this tag to adjust depth perception in crystal. Set between 3 (for close to orthographic) and 30 (for good perspective depth).</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>Nothing, but saves plotly figure to 'crystal_bonds.html'</p>
                        </div>
                    </div>

                    <div class="method" id="get_bond_info">
                        <div class="method-header">
                            <h4>get_bond_info</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3482" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_bond_info(self)</code>
                        </div>
                    </div>

                    <div class="method" id="get_COHP">
                        <div class="method-header">
                            <h4>get_COHP</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3703" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_COHP(self, orbs, NN=None, include_onsite=False, just_one=False)</code>
                        </div>

                        <div class="method-description">
                            <p>Calculates the COHP for the given orbitals and nearest neighbors</p>
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
                                        <td><code>self</code></td>
                                        <td><code>Any</code></td>
                                        <td>An object of the class COGITO_BAND or COGITO_UNIFORM</td>
                                    </tr>
                                    <tr>
                                        <td><code>orbs</code></td>
                                        <td><code>Any</code></td>
                                        <td>either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</td>
                                    </tr>
                                    <tr>
                                        <td><code>NN</code></td>
                                        <td><code>Any</code></td>
                                        <td>An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors</td>
                                    </tr>
                                    <tr>
                                        <td><code>include_onsite</code></td>
                                        <td><code>Any</code></td>
                                        <td>Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>returns COHP values in a [kpt,band] dimension</p>
                        </div>
                    </div>

                    <div class="method" id="get_COOP">
                        <div class="method-header">
                            <h4>get_COOP</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3801" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_COOP(self, orbs, NN=None, include_onsite=False, spin=0)</code>
                        </div>

                        <div class="method-description">
                            <p>Calculates the COHP for the given orbitals and nearest neighbors</p>
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
                                        <td><code>self</code></td>
                                        <td><code>Any</code></td>
                                        <td>An object of the class COGITO_BAND or COGITO_UNIFORM</td>
                                    </tr>
                                    <tr>
                                        <td><code>orbs</code></td>
                                        <td><code>Any</code></td>
                                        <td>either a list of two dictionaries giving elements as keys and orbital types as items (eg [{"Pb":["s","d"],"O":["s","p"]},{"Pb":["s"]"O":["p"]}]) or give list of orb numbers [[1,2,3,5,6,7],[1,2,3,4,5,6,7,8]]</td>
                                    </tr>
                                    <tr>
                                        <td><code>NN</code></td>
                                        <td><code>Any</code></td>
                                        <td>An integer for which nearest neighbor number to include (eg 1 for 1NN) or None or "All" for all nearest neighbors</td>
                                    </tr>
                                    <tr>
                                        <td><code>include_onsite</code></td>
                                        <td><code>Any</code></td>
                                        <td>Includes atomic orbital energy terms (H_ab(R) where R=0 and a=b) instead of just bonding terms</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="returns-section">
                            <h5>Returns</h5>
                            <p>returns COHP values in a [kpt,band] dimension</p>
                        </div>
                    </div>

                    <div class="method" id="get_mulliken_charge">
                        <div class="method-header">
                            <h4>get_mulliken_charge</h4>
                            <div class="source-link">
                                <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3900" target="_blank">source</a>
                            </div>
                        </div>

                        <div class="signature">
                            <code>get_mulliken_charge(self, elem)</code>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <div id="functions" class="tab-content">

        <div class="function-section" id="_cart_to_red">
            <div class="function-header">
                <h2>_cart_to_red</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3947" target="_blank">source</a>
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
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3963" target="_blank">source</a>
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

        <div class="function-section" id="func_for_rad">
            <div class="function-header">
                <h2>func_for_rad</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3978" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>func_for_rad(x, a, b, c, d, e, f, g, h, l)</code>
            </div>
        </div>

        <div class="function-section" id="complex128funs">
            <div class="function-header">
                <h2>complex128funs</h2>
                <div class="source-link">
                    <a href="https://github.com/olipemil/COGITO/blob/main/COGITOico.py#L3981" target="_blank">source</a>
                </div>
            </div>

            <div class="signature">
                <code>complex128funs(phi, theta, sphharm_key)</code>
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
