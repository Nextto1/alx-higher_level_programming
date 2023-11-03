#!/usr/bin/python3

# It prints the number of and the list of its arguments

import sys

argc = len(sys.argv) - 1

if argc == 0:
    print("0 arguments.")
else:
    if argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
