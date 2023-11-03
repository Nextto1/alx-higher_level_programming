#!/usr/bin/python3

def argument_add(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d}".format(num))
        return
    else:
        k = 1
        add = 0
        while k <= num:
            add += int(argv[k])
            k += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    argument_add(sys.argv)
