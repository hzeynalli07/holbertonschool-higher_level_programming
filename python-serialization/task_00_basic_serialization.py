#!/usr/bin/python3
"""Əsas JSON serializasiya modulu."""
import json


def serialize_and_save_to_file(data, filename):
    """Python lüğətini JSON faylına yazır."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """JSON faylını oxuyur və Python lüğətinə çevirir."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
