#!/usr/bin/python3
''' Returns number of lines in a text file '''


def number_of_lines(filename=""):
    '''
    function: number_of_lines

    Args:
        filename (str): file to be opened.

    Returns:
        int: Number of lines.

    '''

    if filename == "" or type(filename) != str:
        return (0)
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return (counter)
