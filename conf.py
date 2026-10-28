# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "reigw-wiki"
copyright = "2026, REIGW Team"
author = "REIGW Team"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
from pathlib import Path

# Load the local domain without installing a separate Python package.
sys.path.insert(0, str(Path(__file__).parent / "_ext"))
extensions = ["igw", "sphinx_rtd_theme"]

templates_path = ["_templates"]
exclude_patterns = [
    ".DS_Store",
    ".pixi",
    "Thumbs.db",
    "_build",
    "_ext",
    "tmp",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Show only the logo in the sidebar's home link.
html_logo = "_static/logo.png"
html_theme_options = {
    "logo_only": True,
    # Keep page scroll restoration from also moving the sidebar on reload.
    "sticky_navigation": False,
}

html_favicon = "_static/favicon.ico"

# Hide the Sphinx and theme footer credit.
html_show_sphinx = False

# Apply the palette after the theme's styles.
html_css_files = ["palette.css"]

# Use syntax highlighting suitable for dark backgrounds.
pygments_style = "monokai"
