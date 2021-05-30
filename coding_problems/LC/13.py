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

# returns the numerical value the given substring corresponds to if it's a roman numeral
# if the substring is not a roman numeral, it returns 0
roman_numerals = {
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
def convert_string_to_single_roman_numeral(s_substring:str) -> int:
    try:
        return roman_numerals[s_substring]
    except KeyError:
        return 0

def romanToInt(s:str) -> int:
    # make a dictionary storing the values for all seven roman numerals
    if (s == ""):
        return 0
    else:
        roman_numeral_value = 0
        sum_of_roman_numerals = 0
        i = len(s)-1
        numerals_to_be_evaluated = ""
        while (i > 0):
            numerals_to_be_evaluated = s[i-1:i+1]
            roman_numeral_value = convert_string_to_single_roman_numeral(numerals_to_be_evaluated)
            if (roman_numeral_value>0):
                if (len(numerals_to_be_evaluated)>1):
                    i -=2
                else:
                    i-=1
                sum_of_roman_numerals += roman_numeral_value
            else: 
                roman_numeral_value = convert_string_to_single_roman_numeral(numerals_to_be_evaluated[1])
                sum_of_roman_numerals += roman_numeral_value
                i -=1
        if (i == 0):
            roman_numeral_value = convert_string_to_single_roman_numeral(s[i])
            sum_of_roman_numerals += roman_numeral_value
        return sum_of_roman_numerals


# roman_numerals = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }
# has constant time, simpler solution
# def romanToInt(s:str) -> int:
#     sum_of_roman_numerals = 0
#     for i in range(0, len(s)):
#         if (s[i] == "V" ) or (s[i] == "X"):
#             if (i>0) and (s[i-1] == "I"):
#                 sum_of_roman_numerals -= 2
#         if (s[i] == "L") or (s[i] == "C"):
#             if (i>0) and (s[i-1] == "X"):
#                 sum_of_roman_numerals -= 20
        
#         if (s[i] == "D") or (s[i] == "M"):
#             if (i>0) and (s[i-1] == "C"):
#                 sum_of_roman_numerals -= 200
#         sum_of_roman_numerals+= roman_numerals[s[i]]
        

#     return sum_of_roman_numerals

# values = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }
# constant time O(1)
# BELOW CODE DOES NOT WORK, DOES NOT PROPERLY ACCOUNT FOR A KEYERROR
# def romanToInt(s: str) -> int:
#     total = 0
#     i = 0
#     while (i < len(s)):
#         # if subtractive case
#         # if at least two symbols remaining AND value of s[i] < value of s[i+1]
#         if (i+1<len(s)) and (values.get(s)[i] < values.get(s)[i+1]):
#                 total += values[s[i+1]] - values[s[i]]
#                 i += 2
#         # Else if not the subtractive case
#         else:
#             i += 1
#             total += values[s[i]]
            
#         # else:
#         #     total = values.get(s)
#     return total
print(romanToInt("III")) #- 3
print(romanToInt("IV")) #- 4
print(romanToInt("IX")) #- 9
print(romanToInt("LVIII")) #58
print(romanToInt("MCMXCIV")) #1994

