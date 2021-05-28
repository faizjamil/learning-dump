# link: https://leetcode.com/problems/roman-to-integer/
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# roman numerals usually written largest to smallest from left to right
# six cases where this is not true
# six cases where subtraction is used
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# given a roman number, convert it to an integer
def romanToInt(s:str) -> int:
    # make a dictionary storing the values for all seven roman numerals
    roman_nummerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    sum_of_roman_numerals = 0
    i = len(s)-1
    test = s[i-1:i+1]
    numerals_to_be_evaluated = ""
    while (i > -1):
        if (i > 0):
            numerals_to_be_evaluated = s[i-1:i+1]
            print(numerals_to_be_evaluated)
        # check if character in front (i-1) is one of six
        # switch statement
        # only perform if i > 0
        # check for special cases
        # else if we are at last character
        # switch
        # case "IV"
        # case "IX"
        # case "XL"
        # case "XC"
        # case "CD"
        # case "CM"
        i-=1

        
    return 0

print(romanToInt("IVX"))