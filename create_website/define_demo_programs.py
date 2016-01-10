#!/usr/bin/env python
# -*- coding: utf-8 -*-

import render_html_demo_programs


def get_definitions():

    programs = render_html_demo_programs.DemoProgramsHtmlCreator()

    define_programs(programs)

    return programs.create()


def define_programs(programs):

    programs.new(
        title='Example: Print hello world',
        name ='ex_print_hello_world',
        type ='example',
        text ='This is your first program, find it at the root base, '
              'run it with this command '
              '<code>pythonw ex_print_hello_world.py</code>',
        )

    programs.new(
        title='Example: Learn how printf works',
        name ='ex_printf_options',
        type = 'example',
        text ='Look at the way <code>printf</code> wraps the line at the end of the screen. '
              'Also look at how you control the color printed. '
              'Take a look at the reversed mode and also '
              'how to make the next line to be printed following the current one',
        )

    programs.new(
        title='Challenge: Draw one line',
        name ='draw_line',
        type ='challenge',
        text ='Can you draw a yellow line in the middle of the screen? (Ana did)'
              'To do it you will need to create a new text file, you can call it '
              '<code>my_python_program.py</code>'
              'and run it with this command '
              '<code>pythonw my_python_program.py</code>',
        )

    programs.new(
        title='Example: Print text and numbers',
        name ='ex_print_text_and_numbers',
        type ='example',
        text ='Look at the way to print numbers inside a string',
        )

    programs.new(
        title='Example: The command <code>input</code>',
        name='ex_input',
        type='example',
        text ='The command <code>input</code> asks you for a texts string or a number'
        )

    programs.new(
        title='Challenge: Sum two numbers',
        name='sum_two_values',
        text ='Can you do that?',
        type='challenge',
    )

    programs.new(
        title='Example: The command <code>if</code>',
        name='ex_if_elif_else',
        type='example',
        text ='The command <code>if</code> checks a condition'
        )


    programs.new(
        title='Challenge: Find the minimum of two numbers',
        name ='minimum_two_values',
        text ='Can you do that?',
        type ='challenge',
    )

    programs.new(
        title='Example: The command <code>while</code>',
        name='ex_while',
        type='example',
        text ='The command <code>while</code> loops until it finds '
              'the command <code>break</code>'
        )

    programs.new(
        name='ex_wait_time',
        title='Example: The command <code>sleep</code>',
        type='example',
        text ='The command <code>sleep</code> stops execution '
                 'for a given number of seconds'
        )
    programs.new(
        title='Challenge: Validation using a loop',
        name='loop_validation',
        text ='Can you do that?',
        type='challenge',
    )
    programs.new(
        title='Challenge: Sum many values entered by user, using a loop',
        name='sum_many_numbers',
        text ='Can you do that?',
        type='challenge',
    )

    programs.new(
        title='Challenge: Find the minimum of many values entered by the user',
        name='minimum_many_values',
        text ='Can you do that?',
        type='challenge',
    )

    programs.new(
        title='Challenge: Make a long word',
        name='long_word',
        text ='Can you do that?',
        type ='challenge'
    )

    programs.new(
        title='Challenge: Squares table',
        name='squares',
        text ='Can you do that?',
        type='challenge'
    )

    programs.new(
        title='Challenge: Exponential table',
        name='exponential',
        type='challenge',
        text ='Can you do that?',
    )

    programs.new(
        title='Challenge: Multiplication table',
        name='mult_table',
        type='challenge',
        text ='Can you do that?',
    )

    programs.new(
        title='Example: Generating random numbers',
        name='ex_random',
        type='example',
        text ='Look at the way to generate random numbers in python'
        )


    programs.new(
        title='Challenge: Guess the number',
        name='guess_the_number',
        type='challenge',
        text ='Can you do that?',
    )

    programs.new(
        title='Example: The command <code>def</code>',
        name='ex_def',
        type='example',
        text ='The command <code>def</code> defines new commands'
        )

    programs.new(
        title='Challenge: Draw a square',
        name ='draw_square',
        type ='challenge',
        text ='Can you do that? Use the def word.',
    )

    programs.new(
        title='Challenge: Draw a right pointing ladder',
        name ='draw_ladder_right',
        type ='challenge',
        text ='Can you do that? Use the def word.',
    )

    programs.new(
        title='Challenge: Draw a left pointing ladder',
        name ='draw_ladder_left',
        type ='challenge',
        text ='Can you do that? Use the def word.',
    )

    programs.new(
        title='Challenge: Draw a pyramid',
        name ='draw_pyramid',
        type ='challenge',
        text ='Can you do that? Use the def word.',
    )



    programs.new(
        title='Example: Start printing in a specific place: xyprint',
        name='ex_xyprintf',
        type ='example',
        text ='xyprintf prints in a fixed position'
        )

    programs.new(
        title='Example: Use the date and time',
        name='ex_date_time',
        type='example',
        text ='Look at the way to obtain the current date and time'
        )
