# link: https://leetcode.com/problems/palindrome-linked-list/
# testing in python shell where palindrome = "131"
# >>> print(palindrome[0:(len(palindrome)//2)+1])
# 13
# >>> print(palindrome[len(palindrome)//2:len(palindrome)])
# 31

from ListNode import ListNode
# Naive solution
def isPalindrome(head: ListNode) -> bool:
    # for now we can go with approach that checks the first half of the string
    # if number is odd
    #     we evaluate the palindrome of the odd number one way
    # else
    #     we slice the string exactly in half
    values = []
    is_palindrome = True
    while (head):
        values.append(head.val)
        head = head.next
    for i in range(0,((len(values)+2-1)//2)):
        left_pointer_index = i
        right_pointer_index = len(values)-1-i
        if (left_pointer_index == right_pointer_index):
            break
        if(values[left_pointer_index]==values[right_pointer_index]):
            is_palindrome = True
        else:
            is_palindrome = False
            break
    return is_palindrome
# head = ListNode(1, ListNode(2,ListNode(2, ListNode(1))))
# head = ListNode(1, ListNode(2,ListNode(3, ListNode(4))))
# head = ListNode(1, ListNode(0,ListNode(0)))
# head = ListNode(1, ListNode(1, ListNode(2, ListNode(1))))
# head = ListNode(1, ListNode(1, ListNode(2, ListNode(1))))
print(isPalindrome(head))
# https://stackoverflow.com/a/54585138