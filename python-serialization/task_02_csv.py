#!/usr/bin/env python3
"""Shebang line indicating the interpreter for the script."""

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as file:
            json.dump(data, file)
        return True
    except FileNotFoundError:
        return False
