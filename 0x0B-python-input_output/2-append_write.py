#!/usr/bin/python3
'''Append text in a file.'''


def append_write(filename="", text=""):
    '''
    Appends text to the end of a UTF8 text file.

    Args:
        filename (str): file to append text on
        text (str): Text to be appended.

    Returns:
        Total number of charaters appended.

    '''

    with open(filename, "a", encoding="utf-8") as file:
        char_count = file.write(text)

        return (char_count)
