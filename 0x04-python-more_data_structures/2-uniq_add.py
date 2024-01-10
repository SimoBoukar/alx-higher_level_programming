#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    uniq_elem = 0
    for i in newlist:
        uniq_elem += i
    return uniq_elem
