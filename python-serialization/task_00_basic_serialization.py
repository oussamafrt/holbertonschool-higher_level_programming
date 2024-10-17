#!/usr/bin/env python3
"""Shebang line indicating the interpreter for the script."""

import json
def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return json.load(file)