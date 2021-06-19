# link: https://leetcode.com/problems/palindrome-linked-list/
# testing in python shell where palindrome = "131"
# >>> print(palindrome[0:(len(palindrome)//2)+1])
# 13
# >>> print(palindrome[len(palindrome)//2:len(palindrome)])
# 31
import ListNode

def isPalindrome(head: ListNode) -> bool:
    # for now we can go with approach that checks the first half of the string
    # if number is odd
    #     we evaluate the palindrome of the odd number one way
    # else
    #     we slice the string exactly in half
    pass