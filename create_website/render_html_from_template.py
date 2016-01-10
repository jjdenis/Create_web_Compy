#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from create_website.settings import WEBSITE_PATH, jinja_environment_templates

def render(name_html, **kwargs):

    template = jinja_environment_templates.get_template(name_html)

    md_text = template.render(**kwargs)

    final_path = WEBSITE_PATH + '{}'.format(name_html)
    f = codecs.open(final_path, 'w', 'utf-8')
    f.write(md_text)
    f.close()

