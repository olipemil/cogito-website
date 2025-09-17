---
layout: default
title: API Documentation
nav_order: 3
has_children: true
---

# COGITO API Documentation

Complete API reference for the COGITO package.

<div class="api-overview">
    <div class="api-card">
        <h3><a href="cogito.html">COGITO Core</a></h3>
        <p>Main COGITO class for running quantum chemistry analysis</p>
    </div>

    <div class="api-card">
        <h3><a href="cogitopost.html">COGITOpost</a></h3>
        <p>Post-processing tools for band structure and bonding analysis</p>
    </div>

    <div class="api-card">
        <h3><a href="cogitoico.html">COGITOico</a></h3>
        <p>Advanced analysis tools and visualizations</p>
    </div>
</div>

## Quick Links

- [Installation Guide](../tutorial/#COGITO)
- [Basic Tutorial](../tutorial/)
- [Examples](../examples/)

<style>
.api-overview {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin: 20px 0;
}

.api-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    flex: 1;
    min-width: 250px;
    transition: box-shadow 0.3s ease;
}

.api-card:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.api-card h3 {
    margin-top: 0;
}

.api-card a {
    text-decoration: none;
    color: #2c5aa0;
}

.source-link, .method-source-link {
    background: #f8f9fa;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 10px 0;
}

.source-link a, .method-source-link a {
    color: #6f42c1;
    text-decoration: none;
    font-size: 0.9em;
}

.source-link a:hover, .method-source-link a:hover {
    text-decoration: underline;
}
</style>
