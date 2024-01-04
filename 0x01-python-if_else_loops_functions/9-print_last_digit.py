#!/usr/bin/python3
def print_last_digit(digit):
    digit = abs(digit) % 10
    print(digit, end="")
    return digit
