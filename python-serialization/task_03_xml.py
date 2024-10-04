#!/usr/bin/python
"""import XLM module"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialise a Python dictionary into XML"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialise an XML file into a Python dictionary."""

    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
