---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

---
layout: default
title: API Documentation
nav_order: 1
parent: API Documentation
---

<style>
/* ReadTheDocs-style API documentation */
.api-section {
    margin: 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

.api-header {
    background: #f6f8fa;
    padding: 16px 20px;
    border-bottom: 1px solid #e1e4e8;
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

.api-signature {
    background: #f8f9fa;
    padding: 12px 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    margin: 12px 0;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
    overflow-x: auto;
}

.api-description {
    padding: 16px 20px;
    background: white;
    line-height: 1.6;
}

.api-parameters {
    background: white;
    padding: 16px 20px;
    border-top: 1px solid #f0f0f0;
}

.api-parameters h5,
.api-parameters h4 {
    color: #2c5aa0;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.api-parameters ul {
    margin: 8px 0;
    padding-left: 0;
    list-style: none;
}

.api-parameters li {
    margin: 8px 0;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border-left: 3px solid #2c5aa0;
}

.api-parameters strong {
    color: #2c5aa0;
    font-weight: 600;
}

.api-parameters code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Class and function headers */
h3 {
    background: linear-gradient(90deg, #f6f8fa 0%, #ffffff 100%);
    padding: 16px 20px;
    margin: 30px 0 20px 0;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 600;
    color: #2c5aa0;
}

h4 {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 20px 0 12px 0;
    border-left: 4px solid #2c5aa0;
    font-size: 16px;
    font-weight: 600;
    color: #1a365d;
}

/* Code blocks */
pre code {
    background: #f6f8fa;
    color: #333;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}

/* Inline code */
p code, li code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    color: #d73a49;
    font-weight: 500;
}

/* Base styles */
p {
    line-height: 1.6;
    margin: 12px 0;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 16px;
    margin: 16px 0;
    color: #666;
    font-style: italic;
}

/* Navigation improvements */
.api-nav {
    background: #f8f9fa;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 20px 0;
}

.api-nav a {
    color: #2c5aa0;
    text-decoration: none;
    font-weight: 500;
}

.api-nav a:hover {
    text-decoration: underline;
}
</style>

# COGITO API Documentation

Complete API reference for the COGITO package - Crystal Orbital Guided Iteration To atomic-Orbitals.

COGITO is a tool for obtaining quantum chemistry from plane wave DFT calculations, enabling analysis of crystal bonding and electronic structure.

# API Reference:

* [COGITO Core Module](https://olipemil.github.io/cogito-website/cogito.html)
  * [`COGITO`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.COGITO)
  * [`func_for_rad()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.func_for_rad)
  * [`func_for_rad_fit()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.func_for_rad_fit)
  * [`func_for_rad_exp()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.func_for_rad_exp)
  * [`lowdin_orth_vectors()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.lowdin_orth_vectors)
  * [`lowdin_orth_vectors_orblap()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.lowdin_orth_vectors_orblap)
  * [`GS_orth_twoLoworthSets()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.GS_orth_twoLoworthSets)
  * [`GS_orth_twoLoworthSets_orblap()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.GS_orth_twoLoworthSets_orblap)
  * [`GS_combine_states_orblap()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.GS_combine_states_orblap)
  * [`complex128funs()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.complex128funs)
  * [`normalize_wf()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.normalize_wf)
  * [`periodic_integral_3d()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.periodic_integral_3d)
  * [`reciprocal_integral()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.reciprocal_integral)
  * [`smooth()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.smooth)
  * [`extract_line_data()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.extract_line_data)
  * [`combine_and_save_plots()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.combine_and_save_plots)
  * [`plot_matrix()`](https://olipemil.github.io/cogito-website/cogito.html#COGITO.plot_matrix)
* [COGITOpost Module](https://olipemil.github.io/cogito-website/cogitopost.html)
  * [`COGITO_TB_Model`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.COGITO_TB_Model)
  * [`COGITO_BAND`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.COGITO_BAND)
  * [`COGITO_UNIFORM`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.COGITO_UNIFORM)
  * [`COGITO_BS_widget`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.COGITO_BS_widget)
  * [`func_for_rad()`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.func_for_rad)
  * [`complex128funs()`](https://olipemil.github.io/cogito-website/cogitopost.html#COGITOpost.complex128funs)
* [COGITOico Module](https://olipemil.github.io/cogito-website/cogitoico.html)
  * [`COGITO_ICO`](https://olipemil.github.io/cogito-website/cogitoico.html#COGITOico.COGITO_ICO)
  * [`func_for_rad()`](https://olipemil.github.io/cogito-website/cogitoico.html#COGITOico.func_for_rad)
  * [`complex128funs()`](https://olipemil.github.io/cogito-website/cogitoico.html#COGITOico.complex128funs)

# Quick Links

* [Main COGITO Repository](https://github.com/olipemil/COGITO)
* [Documentation Website](https://olipemil.github.io/cogito-website)
* [Examples and Tutorials](https://olipemil.github.io/cogito-website/examples/)
