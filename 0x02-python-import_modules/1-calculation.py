#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("Add: {}".format(add(a, b)))
    print("Subtract: {}".format(sub(a, b)))
    print("Multiply: {}".format(mul(a, b)))
    print("Divide: {}".format(div(a, b)))
