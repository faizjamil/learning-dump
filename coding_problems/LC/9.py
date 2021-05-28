# link: https://leetcode.com/problems/palindrome-number/
# check if a number is a palindrome
# if yes return True else return false
# def isPalindrome(x:int) -> bool:
#     #reverse number and check if it's the same as the original
#     #when handling negative sign, we can assume the number is not a palindrome
#     upper_limit = (2**31)-1
#     lower_limit = -(2**31)
#     temp_string = ""
    
#     number_to_reverse = str(x)
#     for i in range(len(number_to_reverse)-1,-1,-1):
#         # if number has a negative sign, add it to the beginning of the reversed number
#         if number_to_reverse[i] != "-":
#             temp_string = temp_string + number_to_reverse[i]
#         else: 
#             return False  
#     reversed_number = int(temp_string)
#     if (reversed_number > upper_limit) or (reversed_number < lower_limit):
#         return False
#     else:
#         return temp_string == number_to_reverse

# print(str(isPalindrome(-101)))
# simple one-liner solution
# def isPalindrome(x:int) -> bool:
#     # check if original string is equal to reversed string
#     # the operation on the right side of equals side reverses string

#     return str(x) == str(x)[::-1]
# solution using math
def isPalindrome(x:int) -> bool:
    if x < 0:
        return False
    reversed_number = 0
    # number % 10 gets you that number
    # subtract the result above from original number
    # divide by 10
    place_value = 0
    while (x //(10**(place_value))) != 0:
        
        reversed_number = (reversed_number*10) + (x //(10**place_value)%10)
        place_value+=1
    return x == reversed_number
print(isPalindrome(121))
# when place_value = 0
# reversed_number = 0 + (121//1) % 10
# reversed_number = 0 + 1
# when place_value = 1
# reversed_number = 1*10 + (121//10)%10
# reversed_number = 10 + 2
# when place_value = 2
# reversed number = 2*10 + ((121//100)%10)