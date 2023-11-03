#!/usr/bin/python3

# The first line prints out sorted
# name from directory
# The last line of code prints out the
# only names that do not start with __

if __name__ == "__main__":
    import hidden_4

    for name in sorted(dir(hidden_4)):

        if name[:2] != '__':
            print("{}".format(name))
