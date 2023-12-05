#!/usr/bin/python3
"""
The read_file function
"""


def read_file(filename=""):
    """""text file(UTF8) is read and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
