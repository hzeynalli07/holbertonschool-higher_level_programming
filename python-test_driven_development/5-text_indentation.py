#!/usr/bin/python3
"""
This module provides a function `text_indentation(text)` that indents text.
It prints a text with 2 new lines after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # İşarələri müəyyən edirik
    delimiters = [".", "?", ":"]
    
    # Simvollar üzərində gəzirik
    i = 0
    # Mətnin başındakı boşluqları təmizləmək üçün flag
    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in delimiters or text[i] == "\n":
            if text[i] in delimiters:
                print("\n")
            
            # Növbəti sətirin əvvəlindəki boşluqları atlayırıq
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
