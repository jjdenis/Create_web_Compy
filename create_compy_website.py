#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser

import create_website.create_the_website

create_website.create_the_website.make_all_html()

print webbrowser.open(
    'file:////Users/jjdenis/Dropbox/Familia/Programas/'
    'ProyectoCompy/web_compy/website/lesson01.html')