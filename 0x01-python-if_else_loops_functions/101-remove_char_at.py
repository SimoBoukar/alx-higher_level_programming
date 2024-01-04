#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for a, b in enumerate(str):
        if a != n:
            str2 += b
    return str2
