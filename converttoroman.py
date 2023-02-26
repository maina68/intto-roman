# funtion to convert int to roman
def int_to_roman(num):
    roman_numeral = ''
    roman_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    for value, symbol in roman_map.items():
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral

# prompt the user to input the integer
num = int(input("Enter an integer:"))

# Convert the integer to roman numerals
roman_numeral = int_to_roman(num)

# Print the roman numeral
print(f"The Roman numeral for {num} is {roman_numeral}")