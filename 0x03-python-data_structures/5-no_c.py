#!/usr/bin/python3
def no_c(my_string):
    my_str = ""
    for k in my_string:
        if (k != 'c') and (k != 'C'):
            my_str += k
    return (my_str)
