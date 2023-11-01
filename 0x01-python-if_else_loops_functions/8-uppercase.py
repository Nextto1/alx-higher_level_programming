#!/usr/bin/python3
def to_upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(string):
    new_string = ""
    for char in string:
        new_string += "%c" % to_upper(char)
    print("{:s}".format(new_string))
