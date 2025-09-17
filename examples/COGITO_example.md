---
layout: default
title: COGITO Example Workflow
parent: Examples
nav_order: 1
---

# COGITO Example Workflow

<div class="notebook-controls">
    <div class="notebook-info">
        <p>📓 Interactive Jupyter notebook example</p>
        <div class="notebook-buttons">
            <a href="https://nbviewer.org/github/olipemil/COGITO/blob/main/COGITO_paper/COGITO_example.ipynb" target="_blank" class="btn btn-primary">📖 View in NBViewer</a>
            <a href="https://github.com/olipemil/COGITO/blob/main/COGITO_paper/COGITO_example.ipynb" target="_blank" class="btn btn-secondary">🔗 View on GitHub</a>
            <a href="https://raw.githubusercontent.com/olipemil/COGITO/main/COGITO_paper/COGITO_example.ipynb" download class="btn btn-success">⬇️ Download Notebook</a>
        </div>
    </div>
</div>

<div class="jupyter-notebook">
    <iframe
        src="https://nbviewer.org/github/olipemil/COGITO/blob/main/COGITO_paper/COGITO_example.ipynb"
        width="100%"
        height="800"
        frameborder="0"
        title="COGITO Example Workflow Jupyter Notebook">
    </iframe>
</div>

<!-- Fallback for if iframe doesn't work -->
<div class="notebook-fallback" style="display: none;">
    <div class="fallback-message">
        <h3>🔧 Notebook Display</h3>
        <p>If the notebook doesn't display above, you can:</p>
        <ul>
            <li><a href="https://nbviewer.org/github/olipemil/COGITO/blob/main/COGITO_paper/COGITO_example.ipynb" target="_blank">View in NBViewer</a> (recommended)</li>
            <li><a href="https://github.com/olipemil/COGITO/blob/main/COGITO_paper/COGITO_example.ipynb" target="_blank">View on GitHub</a></li>
            <li><a href="https://raw.githubusercontent.com/olipemil/COGITO/main/COGITO_paper/COGITO_example.ipynb" download>Download and run locally</a></li>
        </ul>
    </div>
</div>

<style>
.notebook-controls {
    margin: 20px 0;
}

.notebook-info {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
}

.notebook-info p {
    margin: 0 0 10px 0;
    font-weight: 500;
}

.notebook-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.btn {
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
    display: inline-block;
}

.btn-primary {
    background: #2c5aa0;
    color: white;
}

.btn-primary:hover {
    background: #1a365d;
    color: white;
}

.btn-secondary {
    background: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background: #545b62;
    color: white;
}

.btn-success {
    background: #28a745;
    color: white;
}

.btn-success:hover {
    background: #1e7e34;
    color: white;
}

.jupyter-notebook {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px 0;
}

.jupyter-notebook iframe {
    width: 100%;
    min-height: 600px;
    border: none;
}

.fallback-message {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}

.fallback-message h3 {
    margin-top: 0;
    color: #856404;
}

.fallback-message ul {
    margin-bottom: 0;
}

.fallback-message a {
    color: #856404;
    font-weight: 500;
}

/* Responsive design */
@media (max-width: 768px) {
    .notebook-buttons {
        flex-direction: column;
    }

    .jupyter-notebook iframe {
        height: 600px;
    }
}
</style>

<script>
// Show fallback if iframe fails to load
document.addEventListener('DOMContentLoaded', function() {
    const iframe = document.querySelector('.jupyter-notebook iframe');
    const fallback = document.querySelector('.notebook-fallback');

    iframe.addEventListener('error', function() {
        fallback.style.display = 'block';
    });

    // Check if iframe loaded successfully after some time
    setTimeout(function() {
        try {
            if (!iframe.contentDocument && !iframe.contentWindow) {
                fallback.style.display = 'block';
            }
        } catch (e) {
            // Cross-origin restrictions might trigger this
            console.log('Iframe loaded (cross-origin)');
        }
    }, 3000);
});
</script>
