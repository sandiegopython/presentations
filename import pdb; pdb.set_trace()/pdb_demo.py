"""import pdb ; pdb.set_trace() -- An interactive pdb demonstration

To execute this script type::

    python pdb_demo.py
"""

import pdb


def read(s):
    """Do nothing anything at all"""


def write(s):
    """Print out the given string\n"""
    print(s)


def some_function(s):  # Type "n" to get to the next line
    read('Continue execution until function return with "r"')  # Type "r"
    write("This line skipped")  # Type "r" if you haven't already
    write("Another skipped line")
    read('last line')  # Type "n" or "r" again to walk just outside of function


def pdb_test():
    pdb.set_trace()
    read("Continue until next line")  # Type "n" to execute next line
    read('List surrounding lines with "l"')  # Type "l" and then type "n" again
    some_function('Step into functions by typing "s"')  # Type "s" now
    read("We are outside of the function now!")  # Type "n"
    life = 42  # Type "n"
    read('Type "life" to see the value of the variable life')  # Type "n"
    read('Now type "life = 43" to change the value')  # Type "n"
    write("pp can pretty-print things like dictionaries and lists")  # Type "n"
    write('Continue execution by typing "c"')  # Type "c" now
    write('This line and the next one will be skipped since you typed "c"')
    write("Another skipped line")
    write("Oh, and life is now set to: %s" % life)
    write('Done.\n')
    write("More pdb information: http://docs.python.org/2/library/pdb.html\n")

write("import pdb ; pdb.set_trace()")
write("==\n")
write("You are about to begin a journey into pdb\n")
write("Follow instructions on selected lines (lines starting with ->)")
write("The first one is selected below.  Please read and begin.\n")
pdb_test()
pdb.set_trace()
read("One last thing, if you know your program is broken")  # type "n"
read('You can quit with "q"')  # type "q" which will raise bdb.BdbQuit
write("Since you quit, this line won't be printed")
