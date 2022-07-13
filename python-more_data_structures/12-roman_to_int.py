#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) == str or not roman_string:
        return None
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                     "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                     "CD": 400, "CD": 900}
    integer_number = 0
    for i in range(len(roman_string)):
        if roman_string[i:i+2] in sorted(roman_numbers):
            integer_number = integer_number + roman_numbers[roman_string[i:i+2]]
        else:
            integer_number = integer_number + roman_numbers[roman_string[i]]
    return integer_number
