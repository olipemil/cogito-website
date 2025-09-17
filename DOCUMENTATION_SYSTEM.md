# COGITO Website Documentation System

This document describes the enhanced documentation system for the COGITO website with automatic API documentation and Jupyter notebook integration.

## 🏗️ System Architecture

```
COGITO Repository          Website Repository
     │                          │
     ├── COGITO.py               ├── index.md (enhanced)
     ├── COGITOpost.py           ├── api/ (auto-generated)
     ├── COGITOico.py            ├── examples/ (auto-generated)
     └── *.ipynb                 ├── scripts/ (automation)
                                 └── .github/workflows/
```

## 🔄 Auto-Update Workflow

1. **Trigger**: COGITO repository changes
2. **Action**: GitHub Actions detects changes
3. **Process**:
   - Clone latest COGITO code
   - Generate API documentation
   - Convert notebooks to Jekyll pages
   - Commit and deploy changes
4. **Result**: Website automatically updates

## 📁 Key Components

### API Documentation (`/api/`)
- **Auto-generated** from COGITO source code
- **Links to GitHub** for viewing source
- **Interactive navigation** with search
- **Maintains Jekyll styling**

### Examples (`/examples/`)
- **Jupyter notebooks** converted to Jekyll pages
- **Interactive styling** matching website theme
- **Download links** to original notebooks
- **Cross-linked** with tutorials and API docs

### Interactive Homepage
- **Navigation cards** with hover effects
- **Direct links** to tutorials, API docs, and examples
- **API function links** from each demo section
- **Seamless integration** with existing design

## 🚀 Features

### For Users
- **One-click navigation** between tutorials, API docs, and examples
- **Interactive visualizations** preserved from original site
- **Mobile-responsive** design
- **Fast search** and navigation

### For Developers
- **Zero-maintenance** documentation updates
- **Automatic notebook conversion**
- **Cross-repository automation**
- **Version control** for all documentation

## 🛠️ Manual Operations

### Trigger Documentation Update
```bash
# Option 1: GitHub Actions UI
# Go to Actions tab > "Update Documentation from COGITO" > "Run workflow"

# Option 2: API call
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/olipemil/cogito-website/dispatches \
  -d '{"event_type":"cogito-updated"}'
```

### Local Development
```bash
# Generate API docs locally
cd scripts
python3 generate_api_docs.py

# Convert notebooks locally
python3 convert_notebooks.py

# Test Jekyll site
bundle exec jekyll serve
```

## 📝 File Structure

```
cogito-website/
├── api/                    # Auto-generated API docs
│   ├── index.md
│   ├── cogito.md
│   ├── cogitopost.md
│   └── cogitoico.md
├── examples/               # Auto-generated examples
│   ├── index.md
│   ├── cogito_example.md
│   ├── basic_installation_and_setup.md
│   ├── band_structure_analysis.md
│   └── *.md
├── scripts/                # Automation scripts
│   ├── generate_api_docs.py
│   ├── convert_notebooks.py
│   └── setup_webhook.py
├── .github/workflows/      # GitHub Actions
│   └── update-docs.yml
├── index.md               # Enhanced homepage
├── _config.yml            # Updated Jekyll config
└── tutorial/              # Existing tutorials
```

## 🎨 Design Philosophy

### Maintaining Your Vision
- **Preserves** all existing interactive features
- **Enhances** navigation without disrupting UX
- **Extends** hover effects and visual design
- **Integrates** seamlessly with current styling

### Professional Standards
- **Automatic updates** like ReadTheDocs
- **Comprehensive API coverage**
- **Example-driven documentation**
- **Mobile-first responsive design**

## 🔧 Customization

### Adding New Examples
1. Create Jupyter notebook in COGITO repository
2. Push to main branch
3. Website automatically updates

### Modifying API Documentation
1. Update docstrings in COGITO source code
2. Push changes
3. API docs automatically regenerate

### Styling Changes
- Modify CSS in `index.md` or create separate stylesheet
- Changes apply to entire documentation system
- Maintains consistency across all pages

## 🚦 Status Indicators

- ✅ **Operational**: Auto-updates working
- 🔄 **Updating**: Documentation refresh in progress
- ⚠️ **Manual Required**: Trigger update manually
- ❌ **Error**: Check GitHub Actions logs

## 📞 Troubleshooting

### Common Issues
1. **Docs not updating**: Check GitHub Actions logs
2. **Missing API functions**: Verify docstrings in source
3. **Broken links**: Run link checker after updates
4. **Styling issues**: Clear browser cache

### Debug Commands
```bash
# Check workflow status
gh run list --workflow=update-docs.yml

# View logs
gh run view [RUN_ID] --log

# Manual trigger
gh workflow run update-docs.yml
```

---

🎯 **Result**: A professional, automatically-updating documentation website that maintains your unique design while meeting field standards.