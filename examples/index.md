---
layout: default
title: Examples
---

<style>
/* Flex container for the page content */
#page-content {
    display: flex;
    height: 100vh;
    max_width: none;
    width: 135%;
    margin: 0;
    padding: 0;
}

/* Left sidebar styling */
#sideSelect {
    width: 15%;
    background-color: #f0f0f0;
    border-right: 1px solid #ccc;
    overflow-y: auto;
}

/* Material list styling */
#materialList {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

#materialList li {
    padding: 15px;
    cursor: pointer;
    border-bottom: 1px solid #ddd;
}

#materialList li:hover {
    background-color: #e0e0e0;
}

#materialList li.selected {
    background-color: #b0c4de;
    color: #fff;
}

/* Right content area styling */
#content {
    width: 85%;
    overflow: hidden;
}

/* Embedded content styling */
#materialFrame {
    width: 100%;
    height: 100%;
    border: none;
}
</style>

<!-- Page Content -->
<div id="page-content">
    <!-- Left Sidebar -->
    <div id="sideSelect">
        <ul id="materialList">
            <li data-file="Si/bond_cohp_plot.html">Si</li>
            <li data-file="PbO/bond_cohp_plot.html">PbO</li>
            <li data-file="BaFeO3/bond_cohp_plot.html">BaFeO<sub>3</sub></li>
            <li data-file="RbBiO3/bond_cohp_plot.html">RbBiO<sub>3</sub></li>
            <li data-file="K2Sb2O6/bond_cohp_plot.html">KSbO<sub>3</sub></li>
            <li data-file="Pb2Se2O6/bond_cohp_plot.html">PbSeO<sub>3</sub></li>
            <li data-file="Lu4Cr4O12/bond_cohp_plot.html">LuCrO<sub>3</sub></li>
            <li data-file="Na4Ta4O12/bond_cohp_plot.html">NaTaO<sub>3</sub></li>
            <li data-file="Fe16N2.html">Fe<sub>16</sub>N<sub>2</sub></li>
        </ul>
    </div>

    <!-- Right Content Area -->
    <div id="content">
        <iframe id="materialFrame" src=""></iframe>
    </div>
</div>

<script>
    // Get references to elements
    const materialList = document.getElementById('materialList');
    const materials = materialList.getElementsByTagName('li');
    const materialFrame = document.getElementById('materialFrame');

    // Function to handle material selection
    function selectMaterial(event) {
        // Remove 'selected' class from all materials
        for (let i = 0; i < materials.length; i++) {
            materials[i].classList.remove('selected');
        }

        // Add 'selected' class to clicked material
        const selectedMaterial = event.target;
        selectedMaterial.classList.add('selected');

        // Get the data-file attribute to know which file to load
        const fileToLoad = selectedMaterial.getAttribute('data-file');

        // Set the src of the iframe to the selected file
        materialFrame.src = fileToLoad;
    }

    // Attach event listeners to each material
    for (let i = 0; i < materials.length; i++) {
        materials[i].addEventListener('click', selectMaterial);
    }

    // Optionally, select the first material by default
    if (materials.length > 0) {
        materials[0].click();
    }
</script>

