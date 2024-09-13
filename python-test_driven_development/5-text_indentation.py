#!/usr/bin/python3
"""Prints a text with 2 new lines after each '.', '?' and ':'"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in '.?:':
            result += '\n\n'
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result.strip(), end="")
