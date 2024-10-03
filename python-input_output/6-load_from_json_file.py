#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


import json


def load_from_json_file(filename):
    """Function that return a text file"""
    with open(filename) as file:
        return json.load(file)
