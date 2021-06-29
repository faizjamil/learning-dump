# link: https://leetcode.com/problems/integer-to-roman/
# the following function is taken from here: https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/
def get_first_key_by_value(dict, value):
    #list_of_keys = list()
    list_of_items = dict.items()
    if value == 0:
        return ""
    else:
        for item in list_of_items:
            if item[1] == value:
                #list_of_keys.append(item[0])
                return item[0]
    #return list_of_keys
def intToRoman(num: int) -> str:
    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    # how to get roman numerals from integer
    # go through each separate place value integer and lookup in dictionary what roman numeral it corresponds to
    # start from end of integer
    # keep tabs on place value
    # when place value is 0, we want to get the number in the ones places
    # we can convert the integer to a string, have a place_value of 0 to start
    # multiply the number we are on by 10^place_value before looking up the key in the dictionary
    if num == 0 or None:
        return 0
    else:
        num_as_string = str(num)
        roman_numeral_result = ""
        i = len(num_as_string)-1
        place_value = 0
        while (i > -1):
            roman_num_to_append = ""
            current_digit_as_int = int(num_as_string[i])
            key_from_dict = get_first_key_by_value(roman_numerals, (int(num_as_string[i])*10**place_value))
            if (key_from_dict == "" or key_from_dict == None):
                # this means we have a combination of different roman numerals
                if (current_digit_as_int<4 and current_digit_as_int > 0):
                    # that means we have a number between 1 and 3
                    roman_num_to_append = current_digit_as_int *get_first_key_by_value(roman_numerals, 10**place_value)
                elif(current_digit_as_int<9 and current_digit_as_int > 5):
                    # we have a value between 5 and 9, here we will always add a five along with however many         
                    current_digit_as_int = current_digit_as_int-5
                    roman_num_to_append = get_first_key_by_value(roman_numerals, 5*10**place_value) + (current_digit_as_int*get_first_key_by_value(roman_numerals, 10**place_value))
                else:
                    # we have a zero and we just append "" to the roman numeral
                    roman_num_to_append = ""        
            else:
                roman_num_to_append = key_from_dict
            roman_numeral_result = roman_num_to_append + roman_numeral_result
            i = i - 1
            place_value = place_value + 1
        
        return roman_numeral_result

# print(intToRoman(1994))
# correct result: MCMXCIV
# print(intToRoman(58))
# correct result: LVIII
# print(intToRoman(53))
# correct result: LIII
# print(intToRoman(10))
# correct result: X
# print(intToRoman(20))
# correct result: XX
print(intToRoman(60))
# correct result: LX