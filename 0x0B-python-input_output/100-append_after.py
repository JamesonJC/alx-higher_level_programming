#!/usr/bin/python3
''' Insert a line of text after each line in a file of a specific text '''


def append_after(filename="", search_string="", new_string=""):
    '''
    Function inserting text

    Args:
        filename (str): File to insert text in.
        search_string (str): The string to be searched in the file
        new_string (str): The string to be inserted in the file

    '''
    updated_line = []
    with open(filename, "r") as file:
        for line in file:
            update_line.append(line)
            if search_string in line:
                updated_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(updated_lines)
