#!/usr/bin/python3
"""
This module provides a function `text_indentation(text)` that indents text.
It prints a text with 2 new lines after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Mətnin başındakı və sonundakı lazımsız boşluqları kəsirik
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
