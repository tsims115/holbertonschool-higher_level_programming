#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if not isinstance(roman_string, str):
        return 0
    nums = {'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            value = value + nums[roman_string[i]]
            break
        if nums[roman_string[i]] < nums[roman_string[i+1]]:
            value = value + -nums[roman_string[i]]
        else:
            value = value + nums[roman_string[i]]
    return value
