#!/usr/bin/python3
"""Import Module json"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialises the 'data' dictionary in JSON and saves it in the 'filename' file."""

    with open(filename, 'w') as file:
        json.dump(data, filename)


def load_and_deserialize(filename):
    """Loads data from the 'filename' file and deserializes it into a Python dictionary."""

    with open(filename, 'r') as file:
        json.load(filename)
