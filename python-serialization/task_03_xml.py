#!/usr/bin/env python3
"""
Module task_03_xml
Serializes/deserializes Python dict to/from XML using ElementTree.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dict to XML and save to filename.
    Args:
        dictionary (dict): Python dict to serialize.
        filename (str): Output XML file path.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML from filename to Python dict.
    Args:
        filename (str): Input XML file path.
    Returns:
        dict: Reconstructed dictionary (values as str).
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for child in root:
            data[child.tag] = child.text if child.text is not None else ""
        return data
    except (ET.ParseError, FileNotFoundError, IOError):
        return {}
