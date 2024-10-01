#!/usr/bin/python3
"""import_sys-import_os"""

import sys
import os

"""Importing functions from previous files"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

"""If the file exists, loads the list, otherwise initializes an empty list"""
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

"""Add new arguments to the list"""
items.extend(sys.argv[1:])

"""Save the updated list as a JSON file"""
save_to_json_file(items, filename)
