# COGITO Tutorials

These are structured to follow everything you need! The workflow below gives the outline. Click the file labels to quickly get to each section. 

## Insert workflow figure

<h3 id="VASP">Run VASP</h3>

A couple things to keep in mind for the VASP calculation:

* Must be a static run (NSW=0)
* Use an irreducible grid (ISYM=1,2,3)
* Save the wavefunctions (LWAVE=True)
* Use more bands (NBANDS=(8-16)*natoms)
* No spin-orbit coupling (LSORBIT=False, but magnetism is supported (ISPIN=2)

<h3 id="COGITO">Run COGITO</h3>

COGITO reads the INCAR, POSCAR, POTCAR, and WAVECAR files from the VASP calculation. The only required input when calling the COGITOmain class from the user is if the VASP calculation has ISPIN=2 set spin_polar=True. Otherwise, just pass the directory and let the default values handle everything!

COGITO generates the atomic basis and save the tight binding model in three files which will be used to initialize the next step.

* tb_input.txt
* TBparams.txt
* overlaps.txt

Step 1: Install COGITO from link<br>
Run the code below. Because this is a private repository, you will need to use the key I sent via email.

~~~ bash
git clone https://github.com/olipemil/cogito-website.git
# copy COGITO to python path
export PYTHONPATH="${PYTHONPATH}:/COGITO"
~~~

Step 2: Install necessary python packages

~~~ bash
pip install pymatgen
pip install matplotlib
pip install numpy
pip install scipy
pip install lmfit
pip install plotly
pip install seekpath
~~~

Step 3: Run python code to run COGITO

~~~ python
from COGITOmain import COGITO

direct = "Si/"
# create an instance of the COGITO class
COGITOmodel = COGITO(direct) # set "spin_polar = True" for magnetic calculations
# do full algorithm and generate input files for TB model
COGITOmodel.generate_TBmodel(verbose = 0, plot_orbs = True, plot_projBS = True)
~~~

<h3 id="tight">Run COGITO tight binding</h3>

This is where things start to get fun!
Here are some capabilities to plot and verify the COGITO run.

<div style="display: flex; justify-content: space-around;">
    <div style="height: 250px;">
        <img src="{{ site.baseurl }}/docs/Si/compareDFT.png" alt="Image 2" width="90%">
    </div>
    <div style="height: 250px;">
        <img src="{{ site.baseurl }}/docs/Si/tbparams_decay.png" alt="Image 2" width="90%">
    </div>
</div>

<h3 id="bandstruc">Run Bandstructure generator</h3>

This class is for generates a band structure from a default high symmetry line from pymatgen.

<div style="display: flex; justify-content: space-around;">
    <div style="height: 300px;">
        <iframe src="{{ site.baseurl }}/docs/Si/COHP_BS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;"></iframe>
    </div>
    <div style="height: 300px;">
        <iframe src="{{ site.baseurl }}/docs/Si/projectedBS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;"></iframe>
    </div>
</div>

<h3 id="uniform">Run Uniform generator</h3>

This generates a uniform k-point grid, able to perform DOS and itegrated band energy analysis.

<div style="display: flex;">
    <div style="width: 200px;">
        <img src="{{ site.baseurl }}/docs/Si/SiprojectedDOS.png" alt="Image 2" style="width: 100%; height: 100%; border: 0;">
    </div>
    <div style="width: 170px;">
        <img src="{{ site.baseurl }}/docs/Si/COHP_DOS.png" alt="Image 2" style="width: 100%; height: 100%; border: 0;">
    </div>
    <div style="width: 380px;">
        <iframe src="{{ site.baseurl }}/docs/Si/crystal_bonds.html" style="transform: scale(0.75); transform-origin: top left; width: 150%; height: 150%; border: 0;"></iframe>
    </div>
</div>
