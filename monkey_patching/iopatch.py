import sys


class print_to_file:

    """Context manager for sending stdout to a file"""

    def __init__(self, filename):
        stream = open(filename, 'w')
        self.fake_stdout = stream

    def __enter__(self):
        sys.stdout = self.fake_stdout
        return self.fake_stdout

    def __exit__(self, exc_type, exc_value, tracebak):
        sys.stdout.close()
        sys.stdout = sys.__stdout__
