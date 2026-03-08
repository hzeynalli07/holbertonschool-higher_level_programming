#!/usr/bin/python3
"""Faylın sonuna yazı əlavə edən funksiya."""


def append_write(filename="", text=""):
    """Mətni UTF8 formatında fayla əlavə edir və sayını qaytarır."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
