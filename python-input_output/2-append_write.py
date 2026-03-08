#!/usr/bin/python3
"""Faylın sonuna yazı əlavə edən funksiyanı təyin edir."""


def append_write(filename="", text=""):
    """Mətni UTF8 formatında faylın sonuna əlavə edir və simvol sayını qaytarır."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
