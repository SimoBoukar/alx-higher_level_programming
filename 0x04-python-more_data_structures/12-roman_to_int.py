#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    tot = 0
    cte_roman = 'I'
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in reversed(range(len(roman_string))):
        if roman[roman_string[x]] >= roman[cte_roman]:
            cte_roman = roman_string[x]
            tot += roman[roman_string[x]]
        else:
            tot -= roman[roman_string[x]]
    return tot
