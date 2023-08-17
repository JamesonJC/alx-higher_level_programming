#!/usr/bin/python3

def uniq_add(my_list):
    sum_uniq = set()
    for element in my_list:
        if element not in sum_uniq:
            sum_uniq.add(element)
    return [sum(sum_uniq)]
