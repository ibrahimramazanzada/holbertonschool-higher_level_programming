#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(roman_string)):
        value = roman_numerals[roman_string[i]]
        if (
            i + 1 < len(roman_string) and
            value < roman_numerals[roman_string[i + 1]]
        ):
            total -= value
        else:
            total += value
    return total
