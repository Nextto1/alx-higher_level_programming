#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_bool = my_list[:]
    for count, k in enumerate(my_list):
        if k % 2 == 0:
            list_bool[count] = True
        else:
            list_bool[count] = False
    return (list_bool)
