# link: https://leetcode.com/problems/integer-to-english-words/
# for when i want to challange myself (or mmake myself suffer)
from utils import get_first_key_by_value

MAX_VALUE = 2147483647
numbers_to_values = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Eleven": 11,
    "Twelve": 12,
    "Thirteen": 13,
    "Fourteen": 14,
    "Fifteen": 15,
    "Sixteen": 16,
    "Seventeen": 17,
    "Eighteen": 18,
    "Nineteen": 19,
    "Twenty": 20,
    "Thirty": 30,
    "Forty": 40,
    "Fifty": 50,
    "Sixty": 60,
    "Seventy": 70,
    "Eighty": 80,
    "Ninety": 90,
    "Hundred": 100,
    "Thousand": 1000,
    "Million": 1000000,
    "Billion": 1000000000
}
def numberLessThanOneThousandToWords(num: int) -> str:
    # soo we wanna in this case start from the ones place value
    # after we pass the hundreds place value we wanna look at the next three places if they exist
    # if so, then we multiply that by 10000
    # we do a similar thing for million
    num_as_string = ""
    
    # sliding window problem perhaps
    # what we have to do is look at three place values at a time
    # if the number of digits left is < 3, make window that size
    # else the size of the window is three
    # we add window size to place value
    #
    # we grab the window size
    # we get the number, shift window three spaces over
    place_value = len(str(num))-1
    list_of_possible_values = list(numbers_to_values.values())
    for i in reversed(range(len(list_of_possible_values)-3)):
        quotient = num // list_of_possible_values[i]
        if (quotient ==1 ):
            # here we have a number which we need to fetch directly from the dict
            if(place_value == 0):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,list_of_possible_values[i])
            elif(place_value == 2):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " "+ get_first_key_by_value(numbers_to_values, 10**place_value) + " "
                place_value -= 1
            elif(place_value == 1 and i > 19):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,list_of_possible_values[i]) + " "
                place_value -= 1
            elif(place_value == 1 and i == 19):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,list_of_possible_values[i])
                place_value -= 1    
            elif(place_value == 1 and i < 19):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,list_of_possible_values[i]) 
                place_value -= 1
            else:
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " "+ get_first_key_by_value(numbers_to_values, 10**place_value) 
                place_value -= 1
            num = num % list_of_possible_values[i]
            test1 = num
            

        elif (quotient >1 ):
            # this means we have a match, 
            # we grab the first digit, fetch that value, 
            # and multiply it by the value we are at in the list_of_possible_values 
            if num < 100:
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values, quotient*10**place_value) + " "
            else: 
                # test = get_first_key_by_value(numbers_to_values,quotient) + " " + get_first_key_by_value(numbers_to_values, 10**place_value)
                # if place_value == 2 or place_value == 3 or place_value == 6 or place_value == 9:
                #     num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " " + get_first_key_by_value(numbers_to_values, 10**place_value) + " "
                # else:
                #     num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " " + get_first_key_by_value(numbers_to_values, 10**place_value)
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " " + get_first_key_by_value(numbers_to_values, 10**place_value) + " "


            # + get_first_key_by_value(numbers_to_values, list_of_possible_values[i]) + " "
            num = num % (quotient*list_of_possible_values[i])
            test = num
            place_value -= 1
                    # elif (quotient >= 100):

        else: 
            continue
        if (place_value < 0):
            break
    return num_as_string

# print(numberLessThanOneThousandToWords(123456))
def numberToWords(num: int) -> str:
    if num == 0:
        return "Zero"
    num_as_string = str(num)
    num_to_words = ""
    # sliding window problem perhaps
    # what we have to do is look at three place values at a time
    # if the number of digits left is < 3, make window that size
    # else the size of the window is three
    # we add window size to place value
    
    # we grab the window size
    # we get the number, shift window three spaces over
    # place_value = len(num_as_string)-1
    list_of_possible_values = list(numbers_to_values.values())
    # same general procedure as below funciton
    # if we have the quotient as less than one thousand
    window_start = len(num_as_string)
    window_end = window_start
    place_value = 0
    while (window_start > 0 and window_end > 0):
        words_to_add = ""
        # window_end is going to be to the right of window_start
        # in this case we wanna start by subtracting window_start by 3
        # then we pass in the sliced string from window_start to window_end to the helper function
        if (len(num_as_string)-window_start)<3 and (len(num_as_string)-window_start)>0:
            window_start = 0
            window_end = (len(num_as_string)-window_start)
        else:
            window_start -= 3
            #slice string from window_start to window_end
            if (window_start < 0):
                current_window = num_as_string[0:window_end]
            else:
                current_window = num_as_string[window_start:window_end]
                
        # we get the key corresponding to either thousand, million, or billion
        if place_value == 0:
            place_value +=2
        elif place_value == 2:
            place_value +=1
        else:
            place_value += 3
        words_to_add = numberLessThanOneThousandToWords(int(current_window))
        if place_value ==3 or place_value==6 or place_value==9:
            words_to_add =  words_to_add + " "+ get_first_key_by_value(numbers_to_values, 10**place_value) + " "   

        window_end = window_start
        num_to_words = words_to_add + num_to_words
    # for i in reversed(range(len(list_of_possible_values)-4, len(list_of_possible_values))):
    #     # here we look at all numbers below one thousand
    #     quotient = num // list_of_possible_values[i]
    #     if(quotient < 1000 and quotient > 0):
    #         num_as_string = num_as_string + numberLessThanOneThousandToWords(quotient)
    #         # call function
    #         test3 = num_as_string
    #         num = num % 1000
    #     else:
    #         # we take the quotient
    #         continue


    return num_to_words
    # call the funciton below
    # else
    # we floor divide the qyotient by 10**place_value

# print(numberToWords(123))
# correct output: "One Hundred Twenty Three"
# print(numberToWords(12345))
# correct output: ""Twelve Thousand Three Hundred Forty Five""
# print(numberToWords(1234567))
# expected outout: "One Million, Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# print(numberToWords(123456789))
# 1234567891
# correct output: "One billion, two hundred thirty four million, five hundred sixty seven thousand, seven hundred eighty nine"
# print(numberToWords(19))
print(numberToWords(20))
