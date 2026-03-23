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

    .image-container:hover .image-hover {
        opacity: 0.3;
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
        /*pointer-events: auto;  Ensures the div can receive click events */
        transition: opacity 0.3s ease;
    }

    .image-container:hover .overlay-text {
        opacity: 1;
        pointer-events: auto;
    }

    /* New navigation styling */
    .main-navigation {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin: 30px 0;
        justify-content: center;
    }

    .nav-card {
        border: 2px solid #ddd;
        border-radius: 12px;
        padding: 25px;
        flex: 1;
        min-width: 250px;
        max-width: 320px;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        text-align: center;
    }

    .nav-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-color: #2c5aa0;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    }

    .nav-card h3 {
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.3em;
    }

    .nav-card h3 a {
        text-decoration: none;
        color: #2c5aa0;
        display: block;
    }

    .nav-card h3 a:hover {
        color: #1a365d;
    }

    .nav-card p {
        color: #666;
        margin-bottom: 15px;
        font-size: 0.95em;
    }

    .nav-features {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
    }

    .nav-features span {
        background: #e3f2fd;
        color: #1565c0;
        padding: 6px 12px;
        border-radius: 16px;
        font-size: 0.8em;
        font-weight: 500;
        border: 1px solid #bbdefb;
    }

    .nav-card:hover .nav-features span {
        background: #2c5aa0;
        color: white;
        border-color: #2c5aa0;
    }

    /* API links styling */
    .api-links {
        background: #f1f8ff;
        border: 1px solid #c0d3eb;
        border-radius: 8px;
        padding: 12px 20px;
        margin: 15px 0 30px 0;
        text-align: center;
        font-size: 0.9em;
    }

    .api-links a {
        color: #0366d6;
        text-decoration: none;
        font-weight: 500;
        margin: 0 5px;
    }

    .api-links a:hover {
        text-decoration: underline;
        color: #0253ba;
    }

</style>


## Welcome to COGITO!

Crystal Orbital Guided Iteration To atomic-Orbitals (COGITO) is a tool for obtaining quantum chemistry from plane wave DFT calculations. The code maps the plane wave basis to our COGITO basis. With this we can trace back which bonds are contributing to the independent particle energies. Leverging this, we can plot the crystal structure with their actual quantum chemical covalent bonds, determine origins of electronic structure, charge transfer, and more!

<div class="main-navigation">
    <div class="nav-card">
        <h3><a href="{{ site.baseurl }}/tutorial/">Tutorial</a></h3>
        <p>Step-by-step guide to using COGITO</p>
        <div class="nav-features">
            <span>Installation</span>
            <span>Basic Usage</span>
            <span>Advanced Analysis</span>
        </div>
    </div>

    <div class="nav-card">
        <h3><a href="{{ site.baseurl }}/api/">API Documentation</a></h3>
        <p>Complete reference for all COGITO functions</p>
        <div class="nav-features">
            <span>COGITO Core</span>
            <span>Post-processing</span>
            <span>Visualization</span>
        </div>
    </div>

    <div class="nav-card">
        <h3><a href="{{ site.baseurl }}/examples/">Examples</a></h3>
        <p>Interactive Jupyter notebook examples</p>
        <div class="nav-features">
            <span>Workflows</span>
            <span>Tutorials</span>
            <span>Use Cases</span>
        </div>
    </div>
</div>

Observe the bonding in the α-PbO structure by hovering over the bond lines. Solid lines indicate bonding while dashed lines indictate antibonding. The width of the line is proprotional to the magnitude of the bond energy.

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 400px; width: 500px">
        <iframe src="docs/PbO/crystal_bonds.html" style="transform: scale(0.75); transform-origin: top left; width: 150%; height: 150%; border: 0;"></iframe>
    </div>
</div>

## Quick Guide

Click images for detailed tutorials or use the links below to jump directly to API documentation.

<h3 id="tight">Verify quality of COGITO run</h3>

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

<div class="api-links">
    <a href="{{ site.baseurl }}/tutorial/#compareDFT">Tutorial</a> |
    <a href="{{ site.baseurl }}/api/cogitopost.html#compare_to_dft">API: compare_to_DFT</a>
</div>

<h3 id="bandstruc">Plot with band structure k-grid</h3>

<div style="display: flex; justify-content: space-around;">
    <div class="image-container" style="height: 300px;">
        <a href="{{ site.baseurl }}/tutorial/#COHPBS">
            <iframe src="./docs/Si/COHP_BS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
            <div class="overlay-text">Plot projected COHP/COOP</div>
        </a>
    </div>
    <div class="image-container" style="height: 300px;">
        <a href="{{ site.baseurl }}/tutorial/#projectBS">
            <iframe src="./docs/Si/projectedBS.html" style="transform: scale(0.5); transform-origin: top left; width: 200%; height: 200%; border: 0;" class="image-hover"></iframe>
            <div class="overlay-text">Plot orbital projected<br>band structure</div>
        </a>
    </div>
</div>

<div class="api-links">
    <a href="{{ site.baseurl }}/tutorial/#COHPBS">Tutorial</a> |
    <a href="{{ site.baseurl }}/api/cogitopost.html#get_cohp">API: get_COHP</a>, <a href="{{ site.baseurl }}/api/cogitopost.html#get_projectedbs">get_projectedBS</a>
</div>

<h3 id="uniform">Plot with uniform k-grid</h3>

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

<div class="api-links">
    <a href="{{ site.baseurl }}/tutorial/#projectDOS">Tutorial</a> |
    <a href="{{ site.baseurl }}/api/cogitopost.html#get_projecteddos">API: get_projectedDOS</a>, <a href="{{ site.baseurl }}/api/cogitopost.html#get_bonds_figure">get_bonds_figure</a>
</div>  

