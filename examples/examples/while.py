
def my_program():

    clear_screen()

    printf()

    printf('This program shows how "while" works')

    number_of_times = 0

    while number_of_times < 10:

        number_of_times = number_of_times + 1

        printf(number_of_times)





###########################################################################
###########################################################################
# The next lines are needed to run compy, don't mind them,
# but keep them, don't get rid of these lines
###########################################################################
###########################################################################

def clear_screen(): pass

def set_bg_color(color): pass

def set_fm_color(color): pass

def printf(to_print='', color=None, stay=False, reverse=False): pass

def xyprintf(x, y, *args): pass

def poke(x, y, code, color = None, reverse=False): pass

def peek(self, x, y): pass

def input(message = '', color=None): pass

def wait_key(): pass

def check_key(): pass

def redefine_commands(screen):

    global clear_screen, set_bg_color, set_fm_color, printf, xyprintf
    global poke, peek, input, wait_key, check_key

    clear_screen = screen.clear_screen
    set_bg_color = screen.set_bg_color
    set_fm_color = screen.set_fm_color
    printf = screen.printf
    xyprintf = screen.xyprintf
    poke = screen.poke
    peek = screen.peek
    input = screen.input
    wait_key = screen.wait_key
    check_key = screen.check_key

    my_program()

import compy

compy.run(redefine_commands)

###########################################################################
###########################################################################


