# link: https://leetcode.com/problems/integer-to-english-words/
# for when i want to challange myself (or mmake myself suffer)
from utils import get_first_key_by_value

MAX_VALUE = 2,147,483,647
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
    "Fourty": 40,
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
def numberToWords(num: int) -> str:
    num_as_string = ""
    
    # sliding window problem perhaps
    # what we have to do is look at three place values at a time
    # if the number of digits left is < 3, make window that size
    # else the size of the window is three
    # we add window size to place value
    
    # we grab the window size
    # we get the number, shift window three spaces over
    num_as_string = ""
    place_value = len(str(num))-1
    list_of_possible_values = list(numbers_to_values.values())
    # same general procedure as below funciton
    # if we have the quotient as less than one thousand
    test1 = len(list_of_possible_values)
    test2 = len(list_of_possible_values)-4
    test3= reversed(range(len(list_of_possible_values),len(list_of_possible_values)-4))
    for i in reversed(range(len(list_of_possible_values)-3, len(list_of_possible_values))):
        # here we look at all numbers below one thousand
        quotient = num // list_of_possible_values[i]
        if(quotient < 1000 and quotient > 0):
            num_as_string = num_as_string + numberLessThanOneThousandToWords(quotient)
            # call function
            test3 = num_as_string
            num = num % 1000
        else:
            # we take the quotient
            continue

    return num_as_string
    # call the funciton below
    # else
    # we floor divide the qyotient by 10**place_value
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
        if (quotient > 1):
            # this means we have a match, 
            # we grab the first digit, fetch that value, 
            # and multiply it by the value we are at in the list_of_possible_values 
            num_as_string = num_as_string + get_first_key_by_value(numbers_to_values, quotient*place_value) + " "
            # + get_first_key_by_value(numbers_to_values, list_of_possible_values[i]) + " "
            num = num % (quotient*list_of_possible_values[i])
            test = num
            place_value -= 1
        elif (quotient == 1):
            # here we have a number which we need to fetch directly from the dict
            if(place_value < 2):
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,list_of_possible_values[i])  + " "
            else:
                num_as_string = num_as_string + get_first_key_by_value(numbers_to_values,quotient) + " "+ get_first_key_by_value(numbers_to_values, 10**place_value) + " "
            num = num % list_of_possible_values[i]
            test1 = num
            place_value -= 1
        # elif (quotient >= 100):

        else: 
            continue
    return num_as_string

# print(numberLessThanOneThousandToWords(123456))
print(numberToWords(123456))
