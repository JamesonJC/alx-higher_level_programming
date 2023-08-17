#!/usr/bin/python3

def uniq_add(my_list):
    sum_uniq = 0
    for element in set(my_list):
        sum_uniq += element
    return [sum_uniq]
