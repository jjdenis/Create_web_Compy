#!/usr/bin/env python
# -*- coding: utf-8 -*-

from color_table import colors
# from compy.bitmaps import bitmap_images
import tmplt2html
import demoprograms
import settings

def make_all_html():

    copy_images()

    tmplt2html.render('index.html')
    tmplt2html.render('install.html')
    tmplt2html.render('exampleskk.html')
    tmplt2html.render('commands.html')

    examples = define_examples()
    tmplt2html.render('examples.html', challenges=examples)

    challenges = define_challenges()
    tmplt2html.render('challenges.html', challenges=challenges)


    clrs = get_colors()
    tmplt2html.render('colors.html', colors=clrs)

    keys = get_keys()
    tmplt2html.render('keys.html', keys=keys)

    # bitmaps = get_bitmaps()
    # template_to_webpage.t2wp('chars.html', bitmaps=bitmaps)

import os

def copy_images():

    path_chall=settings.CODE_PATH+'challenges/'
    move_files_to_docs(path_chall)

    path_chall=settings.CODE_PATH+'examples/'
    move_files_to_docs(path_chall)


def move_files_to_docs(path_chall):
    files = os.listdir(path_chall)
    for file in files:
        if '.png' in file:
            os.rename(path_chall + file, settings.DOCS_PATH + 'img/' + file)


def define_challenges():

    challenges = demoprograms.DemoPrograms()

    challenges.new(title='Draw one line',
                   name='draw_line',
                   comments='Can you draw a yellow line like the one in this example?',
                   challenge =True)

    challenges.new(title='Sum two numbers',
                   name='sum_two_values',
                   comments='Can you do that?',
                   challenge =True)

    challenges.new(
        name='loop_validation',
        title='Validation using a loop',
        comments='Can you do that?',
        challenge =True)

    challenges.new(
        name='loop_sentinel',
        title='Loop until user finishes',
        comments='Can you do that?',
        challenge =True)

    challenges.new(
        title='Guess the number',
        name='guess_the_number',
        comments='Can you do that?',
        challenge =True)

    return challenges


def define_examples():

    examples = demoprograms.DemoPrograms()

    examples.new(
        name='print_hello_world', title='Print hello world', challenge =False,
        comments='This is your first program: copy the code in a text file, name the file "print_hello_world.py", and '
                 'run it with this command <code>pythonw print_hello_world.py</code>',
        )

    examples.new(
        name='printf_options', title='Learn how printf works', challenge =False,
        comments="""To print in Compy, you can use the command called 'printf'.
printf wraps the line at the end of the screen. With printf you can control the color,
the reversed mode and if the next line will be printed following the current one"""
          )

    examples.new(name='xyprintf', title='Start printing in a specific place: xyprint', challenge =False,
        comments='xyprintf prints in a fixed position'
        )

    examples.new(
        name='print_text_and_numbers', title='print text and numbers', challenge =False,
        comments='Many times you have to print numbers inside a string'
        )

    examples.new(
        name='input', title='The command <code>input</code>', challenge =False,
        comments='The command <code>input</code> asks you for a texts string or a number'
        )

    examples.new(
        name='def', title='The command <code>def</code>', challenge =False,
        comments='The command <code>def</code> defines new commands'
        )

    examples.new(
        name='if_elif_else', title='The command <code>if</code>',  challenge =False,
        comments='The command <code>if</code> checks a condition'
        )

    examples.new(
        name='while', title='The command <code>while</code>',  challenge =False,
        comments='The command <code>while</code> loops until certain condition is met'
        )

    return examples


#
#
# def get_bitmaps():
#     bitmaps = []
#     for bitmap_code, bitmap_path in enumerate(bitmap_images):
#         if bitmap_path:
#             path = bitmap_path.replace('compy/chars', 'chars')
#             bitmaps.append((bitmap_code, path))
#     return bitmaps


def get_keys():
    allowed_keys = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<,.-+'"
    keys = []
    for key_rep in allowed_keys:
        keys.append((ord(key_rep), key_rep))
    keys.append((314, 'left arrow'))
    keys.append((315, 'up arrow'))
    keys.append((316, 'right arrow'))
    keys.append((317, 'down arrow'))
    keys.append((13, 'enter'))
    keys.append((32, 'space'))
    keys.append((396, 'ctrl'))
    keys.append((306, 'upper'))
    keys.append((307, 'alt'))
    keys.append((308, 'command'))
    keys.append((8, 'backspace'))
    return keys

def get_colors():
    clrs = []
    for col_code in range(0, 20):
        col_tup = colors.get_color(col_code)
        html_color = '#{:02X}{:02X}{:02X}'.format(col_tup[0], col_tup[1], col_tup[2])
        clrs.append((col_code,
                     colors.get_color_name(col_code),
                     html_color))
    return clrs




