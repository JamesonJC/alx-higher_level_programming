#!/usr/bin/python3
''' Method reads a file '''


def read_file(filename=""):
    '''
    Method reads a text file (UTF8) and print to stdout.

    Args:
        Filename (str): File to read.

    Returns:
         Nothing.
    '''
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
