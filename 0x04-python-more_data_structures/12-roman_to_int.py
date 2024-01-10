#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roan_string, str):
        return 0
    tot = 0
    cts_roman = 'I'
    roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    for i in reversed(range(len(roman_string))):
        if roman_num[roman_string[i]] >= roman[cts_roman]:
            cts_roman = roman_string[i]
            tot += roman[roman_string[i]]
        else:
            tot -= roman[roman_string[i]]
        return tot
