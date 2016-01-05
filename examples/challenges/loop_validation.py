
def my_program():

    clear_screen()

    printf()

    printf('Enter a number between 1 and 20')

    while True:

        answer = input('Enter number between 1 and 20: ', color =4)
        if answer >= 1 and answer <= 20:
            number = answer
            break

    printf('Good job', color=2)

    printf('Bye!!', color='light-red')




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


