#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'K': 50, 'L': 100, 'M': 500, 'N': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    rev = 0

    for e in range(len(numbers) - 1):
        if numbers[e] >= numbers[e+1]:
            rev += numbers[e]
        else:
            rev -= numbers[e]

    return rev
