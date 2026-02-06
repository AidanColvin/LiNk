# LiNk Repository Structure

This document provides a complete listing of all folders and files in the LiNk repository.

## Root Directory

```
LiNk/
├── .github/              # GitHub configuration
├── .vscode/              # VS Code settings
├── assets/               # Static assets (images, colors)
├── data/                 # Game data files
├── docs/                 # Documentation
├── src/                  # Source code
├── tests/                # Test files
├── LICENSE               # License file
├── Makefile              # Build automation
├── README.md             # Project readme
├── index.html            # Main HTML file
└── start-web.sh          # Web server startup script
```

## Detailed Structure

### .github/
GitHub-specific configuration files
- **workflows/** - GitHub Actions workflows
  - `pages.yml` - GitHub Pages deployment workflow

### .vscode/
VS Code editor settings
- `settings.json` - Editor configuration

### assets/
Static assets for the application

#### assets/colors/
Color palette resources
- `LiNk-color-palette(1).jpg` - Color palette image (version 1)
- `LiNk-color-palette-html-code.html` - HTML color code reference
- `LiNk-color-palette.html` - Interactive color palette

#### assets/images/
Logo and image files
- `LiNk-Logo-HD.jpg` - High-definition logo (JPEG)
- `LiNk-Logo-HD.png` - High-definition logo (PNG)
- `LiNk-logo.jpg` - Standard logo (JPEG)
- `LiNk-logo.pdf` - Logo in PDF format
- `LiNk-logo.png` - Standard logo (PNG)
- `LiNk_logo.webp` - Logo in WebP format

### data/
Game data and configuration files
- `categories.json` - Category definitions
- `master_category_bank.json` - Master bank of all categories organized in batches

### docs/
Documentation files
- `DEPLOY_GITHUB_PAGES.md` - Instructions for GitHub Pages deployment
- `WEB_SETUP.md` - Web setup guide
- `what-needs-to-be-fixed.md` - Issues and items to fix
- `working-httml.md` - Working HTML documentation

### src/
Source code files

#### src/ (Python files)
- `app.py` - Main application file
- `connection_generator.py` - Connection puzzle generator
- `generate_puzzle.py` - Puzzle generation logic
- `main.py` - Main entry point

#### src/modules/
Python modules
- `__init__.py` - Module initialization

### tests/
Test files
- `test_connections.py` - Connection tests
- `test_data.py` - Data validation tests

## Root Files

- **LICENSE** - Apache 2.0 License
- **Makefile** - Build and task automation
- **README.md** - Main project documentation
- **index.html** - Main HTML game interface
- **start-web.sh** - Shell script to start web server

## File Count Summary

- **Total Folders**: 11 (excluding .git and __pycache__)
- **Total Files**: 29 (excluding hidden and cache files)

## Notes

- `.git/` - Git version control directory (hidden)
- `__pycache__/` - Python bytecode cache (auto-generated)
- This structure represents the current state of the repository

Last updated: 2026-02-06
