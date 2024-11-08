import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    """Reads and parses data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])  # Convert id to integer
                row['price'] = float(row['price'])  # Convert price to float
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data
