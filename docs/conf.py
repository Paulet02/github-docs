# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'QSimov Cloud Client'
copyright = '2023, QSimov Quantum Computing S.L.'
author = 'QSimov Quantum Computing S.L.'
release = '0.0.1'


import mock

MOCK_MODULES = ['numpy', 'sympy', 'json', 'logging', 're', 'requests']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'nbsphinx'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "_static/QSimov.svg"

html_theme_options = {
    "collapse_navigation": True
}
html_context = {
  'display_github': True,
  'github_user': 'QSimovTech',
  'github_repo': 'qsimov-cloud-client',
  'github_version': 'main/docs/'
}
html_sidebars = {
    "**": ["search-field", "sidebar-nav-bs"]  # remove ads
}
