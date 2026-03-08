#!/usr/bin/python3
"""Obyekti JSON olaraq fayla yazan funksiya."""
import json


def save_to_json_file(my_obj, filename):
    """Obyekti JSON təmsili ilə mətn faylına yazır."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
