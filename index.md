---
layout: default
title: COGITO - Home
---

## Welcome to COGITO

Your welcome statement and introduction goes here...

[Home](./index.md)

[Functionality](./functionality.md)

[Workflow](./workflow.md)


## Main Code

The core of COGITO is responsible for generating the basis and constructing the tight-binding (TB) model. This is the foundational step in the workflow, where the primary calculations and basis functions are established.

## Plot Wannier Functions

COGITO provides the functionality to visualize Wannier functions, allowing users to gain insights into the electronic structure and orbital interactions within the material.


## Workflow Overview

The COGITO workflow involves a series of steps that start from the VASP calculations and proceed through the tight-binding model construction to the plotting of band structures and densities of states (DOS).

![COGITO Workflow](workflow_image.png)
*Figure 1: COGITO Workflow Diagram*

## 1. Static VASP Calculation

Initial calculations are performed using VASP with an indelible uniform grid. This provides the necessary data for generating the tight-binding model.



