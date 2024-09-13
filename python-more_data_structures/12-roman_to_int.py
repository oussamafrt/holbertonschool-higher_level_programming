#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total, prev_value = 0
    for char in roman_string:
        value = roman_numbers[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total
