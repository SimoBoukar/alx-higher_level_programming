#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest_mark = 0
    best_key = None
    for i, j in a_dictionary:
        if j > highest_mark:
            highest_mark = j
            best_key = i
    return best_key
