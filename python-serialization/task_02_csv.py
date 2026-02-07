#!/usr/bin/env python3
"""
Convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read data from a CSV file and write it to data.json in JSON format.
    Return True on success, False on failure.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
