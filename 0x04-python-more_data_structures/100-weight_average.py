#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        diviser = 0
        for tupl in my_list:
            n += (tupl[0] * tupl[1])
            diviser += tupl[1]
        return (n/diviser)
    return (0)
