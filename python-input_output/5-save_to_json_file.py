#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


import json


def save_to_json_file(my_obj, filename):
    """Function that return a text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
