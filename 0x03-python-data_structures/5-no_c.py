#!/usr/bin/env python3
def no_c(my_string):
    none = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            none += my_string[x]
    return none
