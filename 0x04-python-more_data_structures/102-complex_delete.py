#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    mvp = a_dictionary.copy()
    for e, v in mvp.items():
        if value == v:
            a_dictionary.pop(e)
    return a_dictionary
