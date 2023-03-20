# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Fundamentals'
copyright = '2023, Kristian Rother'
author = 'Kristian Rother'
release = '0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ls'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_path = ['themes']
html_static_path = ['_static']
#html_logo = "_static/academis-header.png"
html_favicon = "_static/favicon.ico"
html_title = "Python Fundamentals"

html_theme_options = {
    "sidebar_hide_name": False,
    "source_repository": "https://github.com/krother/python_fundamentals_nobleprog/",
    "source_branch": "main",
    "source_directory": "/",

    "light_css_variables": {
        # see https://github.com/pradyunsg/furo/tree/main/src/furo/assets/styles/variables
        "color-card-background": "#80b940",
        "color-background-secondary": "#d3e7a9",  # "#b3d789",
    },
}

todo_include_todos = False
