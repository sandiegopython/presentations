"""import pdb ; pdb.set_trace() -- An interactive pdb demonstration

To execute this script type::

    python pdb_demo.py
"""


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
    import pdb ; pdb.set_trace()
    read("continue until next line")  # Type "n" to execute next line
    read('list surrounding lines with "l"')  # Type "l" and then type "n" again
    some_function('step into functions by typing "s"')  # Type "s" now
    read("We are outside of the function now!")  # Type "n"
    write('continue execution by typing "c"')  # Type "c" now
    write('This line and the next one will be skipped since you typed "c"')
    write("Another skipped line")
    write('Done.\n')
    write("more pdb information: http://docs.python.org/2/library/pdb.html\n")

write("import pdb ; pdb.set_trace()")
write("==\n")
write("You are about to begin a journey into pdb\n")
write("Follow instructions on selected lines (lines starting with ->)")
write("The first one is selected below.  Please read and begin.\n")
pdb_test()
