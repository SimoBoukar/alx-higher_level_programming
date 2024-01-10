#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str and None:
        return 0
    num = 0
    tot = 0
    roman_num = ('I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000)
    for i in reversed(roman_string):
        num = roman_num[i]
        tot += num if tot < num * 5 else -num
    return tot
