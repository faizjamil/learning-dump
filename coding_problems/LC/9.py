# link: https://leetcode.com/problems/palindrome-number/
# check if a number is a palindrome
# if yes return True else return false
def isPalindrome(x:int) -> bool:
    #reverse number and check if it's the same as the original
    #when handling negative sign, we can assume the number is not a palindrome
    upper_limit = (2**31)-1
    lower_limit = -(2**31)
    temp_string = ""
    
    number_to_reverse = str(x)
    for i in range(len(number_to_reverse)-1,-1,-1):
        # if number has a negative sign, add it to the beginning of the reversed number
        if number_to_reverse[i] != "-":
            temp_string = temp_string + number_to_reverse[i]
        else: 
            return False  
    reversed_number = int(temp_string)
    if (reversed_number > upper_limit) or (reversed_number < lower_limit):
        return False
    else:
        return temp_string == number_to_reverse

print(str(isPalindrome(-101)))