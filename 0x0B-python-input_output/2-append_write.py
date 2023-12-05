#!/usr/bin/python3
"""
It appends a string
"""


def append_write(filename="", text=""):
    with open(filename, 'k', encoding='utf=8') as f:
        return f.write(text)
