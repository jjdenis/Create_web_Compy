#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from string import Template
import codecs
import pygments
# from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

import settings

Composed = namedtuple('Composed', ['html', 'jquery'], verbose=False)

class DemoProgramsHtmlCreator(object):

    def __init__(self):
        self.programs = []

    def new(self, title, name, text, type):
        dp = OneDemoProgramHtmlCreator(title, name, text, type)
        self.programs.append(dp)

    def create(self):
        composed = []
        for program in self.programs:
            html = program.compose_html()
            jquery = program.compose_jquery()
            one_composed = Composed(html, jquery)
            composed.append(one_composed)
        return composed



class OneDemoProgramHtmlCreator(object):

    def __init__(self, title, name, comments, type):
        self.title = title
        self.name = name
        self.comments = comments
        self.type = type

    def compose_html(self):
        code = self.get_code(self.name, self.type)
        code_html = self.code2html(code)
        html = example_template.substitute(
            name=self.name,
            title=self.title,
            comments=self.comments,
            code=code_html,
            )
        return html

    def get_code(self, name, type):
        path=''
        if type=='challenge':
            path = settings.CHALLENGES_PATH
        else:
            path = settings.EXAMPLES_PATH
        fn = path + '{}.py'.format(name)

        f = codecs.open(fn, 'r', 'utf-8')
        code = f.read()
        f.close()
        return code

    def code2html(self, code):
        code_html = pygments.highlight(code, PythonLexer(), HtmlFormatter())
        return code_html

    def compose_jquery(self):
        jq = jquery_template.format(name=self.name)
        return jq




example_template = Template("""

        <h2 id="$name "> $title </h2>

            <p> $comments </p>

            <p><img src="img/${name}.png" alt="" /></p>

            <button class="$name "> Solution </button>

            <div class="code $name "><code> $code </code></div>

            <hr/>
""")

jquery_template = """

$("div.{name} ").hide();
$("button.{name} ").click(function(){{ $("div.{name} ").toggle();  }});

"""

