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


## Welcome to COGITO

Your welcome statement and introduction goes here...

[Home](./index.md)

[Functionality](./functionality.md)

[Workflow](./workflow.md)


## Main Code

The core of COGITO is responsible for generating the basis and constructing the tight-binding (TB) model. This is the foundational step in the workflow, where the primary calculations and basis functions are established.

# Workflow

<iframe src="./workflow_diagram.html" width="800" height="400" style="border:none;"></iframe>

## Quick Guide 

Click link for more detailed example in the tutorial page.

### Run VASP

A couple things to keep in mind for the VASP calculation:

* Must be a static run (NSW=0)
* Use an irreducible grid (ISYM=1,2,3)
* Save the wavefunctions (LWAVE=True)
* Use more bands (NBANDS=(8-16)*natoms)
* No spin-orbit coupling (LSORBIT=False, but magnetism is supported (ISPIN=2)

### Run COGITO

COGITO reads the INCAR, POSCAR, POTCAR, and WAVECAR files from the VASP calculation. The only required input when calling the COGITOmain class from the user is if the VASP calculation has ISPIN=2 set spin_polar=True. Otherwise, just pass the directory and let the default values handle everything!

COGITO generates the atomic basis and save the tight binding model in three files which will be used to initialize the next step.

* tb_input.txt
* TBparams.txt
* overlaps.txt

### Run COGITO tight binding

This is where things start to get fun!
Here are some capabilities to plot and verify the COGITO run.

<div style="display: flex; justify-content: space-around;">
    <div class="image-container">
        <img src="./overlaps_decay.png" alt="Image 1" width="90%" class="image-hover">
    <div class="overlay-text">Plot overlap decay</div>
    </div>
    <div class="image-container">
        <img src="./tbparams_decay.png" alt="Image 2" width="90%" class="image-hover">
        <div class="overlay-text">Plot hopping decay</div>
    </div>
    <div class="image-container">
        <img src="./compareDFT.png" alt="Image 2" width="90%" class="image-hover">
        <div class="overlay-text">Compare COGITO bands<br>to VASP</div>
    </div>
</div>

<div style="display: flex; justify-content: space-around;">
    <img src="./overlaps_decay.png" alt="Image 1" width="30%">
    <img src="./tbparams_decay.png" alt="Image 2" width="30%">
    <img src="./compareDFT.png" alt="Image 3" width="30%">
</div>

### Run Bandstructure generator

This class is for generates a band structure from a default high symmetry line from pymatgen. 

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 600px;">
        <iframe src="./COHP_BS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
    <div class="overlay-text">Plot projected COHP/COOP</div>
    </div>
    <div class="image-container" style="height: 600px;">
        <iframe src="./projectedBS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
        <div class="overlay-text">Plot orbital projected<br>band structure</div>
    </div>
</div>


## 1. Static VASP Calculation

Initial calculations are performed using VASP with an indelible uniform grid. This provides the necessary data for generating the tight-binding model.



