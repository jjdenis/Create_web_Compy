#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader

SAVE_TO_DOCS_PATH = True

WEBSITE_PATH   = u'website/'
SCREENSHOTS_PATH = u'website/img/'
EXAMPLES_PATH   = u'/Users/jjdenis/Dropbox/Familia/Programas/ProyectoCompy/compy/'
CHALLENGES_PATH   = u'challenges/'

jinja_environment_templates = Environment(loader=PackageLoader('create_website', 'templates'))
