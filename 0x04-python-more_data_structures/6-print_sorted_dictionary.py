#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for c in sorted(my_dict.keys()):
        print("{}: {}".format(c, my_dict[c]))
