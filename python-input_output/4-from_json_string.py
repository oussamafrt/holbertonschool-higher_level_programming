#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


import json


def from_json_string(my_str):
    """Function that return a text file"""
    return json.loads(my_str)
