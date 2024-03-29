#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    old_items = []

old_items.extend(arglist)
save_to_json_file(old_items, "add_item.json")
