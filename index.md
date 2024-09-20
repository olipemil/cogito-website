---
layout: default
title: COGITO - Home
---

<style>
    .image-container {
        position: relative;
        display: inline-block;
    }

    .image-hover {
        transition: opacity 0.3s ease;
        display: block;
    }

    .image-hover:hover {
        opacity: 0.3;
    }

    .overlay-text {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%; 
        display: flex; 
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 16px;
        font-weight: bold;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
    }

    .image-container:hover .overlay-text {
        opacity: 1;
    }
</style>


## Welcome to COGITO!

Crystal Orbital Guided Iteration To atomic-Orbitals (COGITO) is a tool for obtaining quantum chemistry from plane wave DFT calculations. The code maps the plane wave basis to our COGITO basis. With this we can trace back which bonds are contributing to the independent particle energies. Leverging this, we can plot the crystal structure with their actual quantum chemical covalent bonds, determine origins of electronic structure, charge transfer, and more!

Observe the bonding in the α-PbO structure by hovering over the bond lines. Solid lines indicate bonding while dashed lines indictate antibonding. The width of the line is proprotional to the magnitude of the bond energy.

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 400px; width: 500px">
        <iframe src="docs/PbO/crystal_bonds.html" style="transform: scale(0.75); transform-origin: top left; width: 150%; height: 150%; border: 0;"></iframe>
    </div>
</div>

## Workflow

<iframe src="{{ site.baseurl }}/workflow_diagram.html" style="transform: scale(0.9); transform-origin: top left;" width="800px" height="450px"></iframe>

## Quick Guide 

Click link for more detailed example in the tutorial page.

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

<h3 id="tight">Run COGITO tight binding</h3>

This is where things start to get fun!
Here are some capabilities to plot and verify the COGITO run.

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 250px;">
        <a href="{{ site.baseurl }}/tutorial/#compareDFT">
            <img src="./docs/Si/compareDFT.png" alt="Image 2" width="90%" class="image-hover">
            <div class="overlay-text">Compare COGITO bands<br>to VASP</div>
        </a>
    </div>
    <div class="image-container" style="height: 250px;">
        <a href="{{ site.baseurl }}/tutorial/#tight">
            <img src="./docs/Si/tbparams_decay.png" alt="Image 2" width="90%" class="image-hover">
            <div class="overlay-text">Plot parameter decay</div>
        </a>
    </div>
</div>

<h3 id="bandstruc">Run Bandstructure generator</h3>

This class is for generates a band structure from a default high symmetry line from pymatgen. 

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 300px;">
        <iframe src="./docs/Si/COHP_BS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
        <a href="{{ site.baseurl }}/tutorial/#COHPBS">
            <div class="overlay-text">Plot projected COHP/COOP</div>
        </a>
    </div>
    <div class="image-container" style="height: 300px;">
        <iframe src="./docs/Si/projectedBS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
        <div class="overlay-text"><a href="{{ site.baseurl }}/tutorial/#projectBS">Plot orbital projected<br>band structure</a></div>
    </div>
</div>

<h3 id="uniform">Run Uniform generator</h3>

This generates a uniform k-point grid, able to perform DOS and itegrated band energy analysis.

<div style="display: flex;">
    <div class="image-container" style="width: 200px;">
        <a href="{{ site.baseurl }}/tutorial/#projectDOS">
            <img src="./docs/Si/SiprojectedDOS.png" alt="Image 2" style="width: 100%; height: 100%; border: 0;" class="image-hover">
            <div width="100%" class="overlay-text">Plot orbital<br>projected DOS</div>
        </a>
    </div>
    <div class="image-container" style="width: 170px;">
        <img src="./docs/Si/COHP_DOS.png" alt="Image 2" style="width: 100%; height: 100%; border: 0;" class="image-hover">
        <div class="overlay-text">Plot COHP/COOP energy density</div>
    </div>
    <div class="image-container" style="width: 380px;">
        <a href="{{ site.baseurl }}/tutorial/#bonds">
            <iframe src="docs/Si/crystal_bonds.html" style="transform: scale(0.75); transform-origin: top left; width: 150%; height: 150%; border: 0;" class="image-hover"></iframe>
            <div class="overlay-text">Plot crytstal with COGITO bonds</div>
        </a>
    </div>
</div>  

