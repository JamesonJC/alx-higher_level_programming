#!/usr/bin/python3
''' Write a text into a file '''


def write_file(filename="", text=""):
    '''
    function: write_file

    Args:
        filename (str): file to write into.
        text (str): Text to be written.

    Returns:
        int: Number of characters written.

    '''

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
