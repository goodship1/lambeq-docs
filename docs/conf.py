# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import os
from lambeq import __version__ as version, __version_info__ as v
trim_version = f'{v[0]}.{v[1]}.{v[2]}'
if version.startswith(f'{trim_version}.'):
    version = f'{v[0]}.{v[1]}.{int(v[2]) - 1} [git latest]'
release = version


project = 'lambeq'
author = 'Quantinuum QNLP Dev Team'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',
    'sphinx_mdinclude',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinxarg.ext',
    'sphinx_copybutton',
    'sphinxcontrib.jquery',
    'sphinxcontrib.bibtex',
    'myst_nb',
    "sphinxcontrib.googleanalytics",
]

intersphinx_mapping = {
    'discopy': ("https://docs.discopy.org/en/main/", None),
    'pennylane': ("https://pennylane.readthedocs.io/en/stable/", None),
}

autodoc_default_options = {
    'members': True,
    'inherited-members': True,
    'undoc-members': True,
    'special-members': '__init__, __call__',
}

# This disables the need to document methods in the class docstring.
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', 'quantinuum-sphinx/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
  'navigation_depth': -1
}
html_context = {
  'display_github': True,
  'github_user': 'CQCL',
  'github_repo': 'lambeq',
  'github_version': 'main',
  'conf_py_path': '/docs/'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
quantinuum_sphinx_path = username = os.getenv("QUANTINUUM_SPHINX_PATH", "quantinuum-sphinx")
html_static_path = [f'{quantinuum_sphinx_path}/_static', '_static']
html_favicon = f'{quantinuum_sphinx_path}/_static/assets/quantinuum_favicon.svg'
html_title = f'λambeq {release}'

# CSS for allowing text wrapping within table cells
html_css_files = [
    'css/table-wrap.css',
    'css/sidebar-title.css',
]

def autodoc_skip_member(app, what, name, obj, skip, options):
    if name == 'Symbol':
        options['inherited-members'] = False
        return False
    return skip


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


numfig = True


autosectionlabel_prefix_document = True
myst_enable_extensions = ["dollarmath", "html_image", "attrs_inline", "colon_fence"]
nb_execution_mode = "off"
myst_heading_anchors = 4


bibtex_bibfiles = ['references.bib']

googleanalytics_id = "G-YPQ1FTGDL3"
