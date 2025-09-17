---
layout: default
title: Examples
nav_order: 4
has_children: true
---

# COGITO Examples

Interactive Jupyter notebook examples demonstrating COGITO's capabilities. All examples are based on the comprehensive COGITO tutorial notebook.

<div class="examples-grid">
    <div class="example-card">
        <h3><a href="installation_setup.html">Installation & Setup</a></h3>
        <p>Get started with COGITO installation and environment setup</p>
        <div class="example-tags">
            <span class="tag">Getting Started</span>
            <span class="tag">Dependencies</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="basic_analysis.html">Basic Analysis</a></h3>
        <p>Core COGITO workflows: verification, band structure, and validation</p>
        <div class="example-tags">
            <span class="tag">Band Structure</span>
            <span class="tag">Verification</span>
        </div>
    </div>

    <div class="example-card">
        <h3><a href="advanced_features.html">Advanced Features</a></h3>
        <p>COHP analysis, bonding visualization, and crystal chemistry</p>
        <div class="example-tags">
            <span class="tag">COHP</span>
            <span class="tag">3D Visualization</span>
            <span class="tag">Bonding</span>
        </div>
    </div>
</div>

## Getting Started

1. **[Download examples](https://github.com/olipemil/COGITO/tree/main/examples)** from the COGITO repository
2. **Install dependencies** using the [installation guide](../tutorial/#COGITO)
3. **Run notebooks** in your local Jupyter environment

<div class="getting-started-note">
💡 <strong>Tip:</strong> All examples are designed to work with the sample data included in the COGITO repository.
</div>

<style>
.examples-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin: 30px 0;
}

.example-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    transition: all 0.3s ease;
    background: white;
}

.example-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}

.example-card h3 {
    margin-top: 0;
    margin-bottom: 10px;
}

.example-card h3 a {
    text-decoration: none;
    color: #2c5aa0;
}

.example-card h3 a:hover {
    text-decoration: underline;
}

.example-card p {
    color: #666;
    margin-bottom: 15px;
}

.example-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    background: #e9ecef;
    color: #495057;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.85em;
    font-weight: 500;
}

.getting-started-note {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    border-radius: 4px;
    padding: 15px;
    margin: 20px 0;
}
</style>
