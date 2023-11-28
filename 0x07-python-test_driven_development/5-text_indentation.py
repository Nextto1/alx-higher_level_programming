#!/usr/bin/python3
"""
This module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("it must be a string")
    flag = 0
    for k in text:
        if flag == 0:
            if k == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if k == '?' or k == '.' or k == ':':
                print(k)
                print()
                flag = 0
            else:
                print(k, end="")
