#!/usr/bin/python3
"""Obyekti JSON string-ə çevirən funksiya."""
import json


def to_json_string(my_obj):
    """Obyektin JSON təmsilini (string) qaytarır."""
    return json.dumps(my_obj)
