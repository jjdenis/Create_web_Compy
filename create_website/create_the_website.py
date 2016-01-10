#!/usr/bin/env python
# -*- coding: utf-8 -*-

from color_table import colors
# from compy.bitmaps import bitmap_images
import render_html_from_template
import define_demo_programs
import move_images

def make_all_html():

    move_images.copy_images()

    render_html_from_template.render('index.html')
    render_html_from_template.render('install.html')
    render_html_from_template.render('exampleskk.html')
    render_html_from_template.render('commands.html')

    programs = define_demo_programs.get_definitions()
    render_html_from_template.render('lesson01.html', programs=programs)

    clrs = get_colors()
    render_html_from_template.render('colors.html', colors=clrs)

    keys = get_keys()
    render_html_from_template.render('keys.html', keys=keys)

    # bitmaps = get_bitmaps()
    # template_to_webpage.t2wp('chars.html', bitmaps=bitmaps)


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




