#!/usr/bin/python3
def max_integer(my_list=[]):
    sorted_list = my_list.sort()
    max_value = sorted_list.pop()
    return max_value
