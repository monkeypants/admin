# -*- coding: utf-8 -*-
#
# CanberrraUAV Administrivia documentation build configuration file, created by
# sphinx-quickstart on Mon Feb 25 21:28:16 2013.
#

import sys, os


# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.todo', 'sphinxcontrib.spelling']

spelling_lang='en_AU'
spelling_word_list_filename='OK_wordlist.txt'
spelling_show_suggestions=True

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'CanberrraUAV Administrivia'
copyright = u'2013, CanberraUAV Team'

version = '0.1'
release = '0.1'
exclude_trees = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'CanberrraUAVAdministriviadoc'

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
  ('index', 'CanberrraUAVAdministrivia.tex', u'CanberrraUAV Administrivia Documentation',
   u'CanberraUAV Team', 'manual'),
]


