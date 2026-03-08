#!/usr/bin/python3
"""JSON string-i obyektə çevirən funksiya."""
import json


def from_json_string(my_str):
    """JSON string-dən Python obyekti qaytarır."""
    return json.loads(my_str)
