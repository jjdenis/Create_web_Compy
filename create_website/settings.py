#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Two modes of operation, if True, it helps with website
# this is for development.
# If false, the screenshots will be in the base path.
# This is for use after pip install
from jinja2 import Environment, PackageLoader

SAVE_TO_DOCS_PATH = True

DOCS_PATH   = u'/Users/jjdenis/Dropbox/Familia/Programas/ProyectoCompy/web_compy/website/'
SSHOTS_PATH = u'/Users/jjdenis/Dropbox/Familia/Programas/ProyectoCompy/web_compy/website/img/'
CODE_PATH   = u'/Users/jjdenis/Dropbox/Familia/Programas/ProyectoCompy/web_compy/examples/'

jinja_environment_templates = Environment(loader=PackageLoader('create_website', 'templates'))