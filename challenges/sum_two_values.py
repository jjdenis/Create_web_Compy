
def my_program():

    clear_screen()

    printf()
    printf('SUM TWO NUMBERS', color=4)
    printf('===============')
    printf()

    first_value = input("Give me one number: ", color=8)

    second_value = input("Give me another number: ")

    sum_of_values = first_value + second_value

    response = 'The sum of {} and {} is {}'.format(first_value, second_value, sum_of_values)

    printf()
    printf(response, color=6)





###########################################################################
###########################################################################
# The next lines are needed to run compy, don't mind them,
# but keep them, don't get rid of these lines
###########################################################################
###########################################################################
import compy
import time

# define commands of compy, so IDE's will recognize them
def clear_screen(): pass
def set_bg_color(color): pass
def set_fm_color(color): pass
def printf(to_print='', color=None, stay=False, reverse=False): pass
def xyprintf(x, y, *args): pass
def poke(x, y, code, color = None, reverse=False): pass
def peek(self, x, y): pass
def input(message = '', color=None): return None
def wait_key(): pass
def check_key(): pass

def redefine_commands_and_run(screen):

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

if __name__ == '__main__':
    compy.run(redefine_commands_and_run)

###########################################################################
###########################################################################

