# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import ListNode


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    sumList = l1
    while (sumList or l2 is not None):

        sumList.val = sumList.val + l2.val
        sumList = sumList.next
        l2 = l2.next
    return sumList
# driver code
list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4)))
main = addTwoNumbers(None, list1, list2)
print(main)