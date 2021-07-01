class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    """
    TODO: ADD FUNCTION TO REVERSE LINKED LIST
    """
    def addNode(self, data):
        while (self.next != None):
            self = self.next
        new_node = ListNode(data)
        self.next = new_node
        return self
    def reverseLinkedList(self):
        ll_as_array = []
        while(self.next != None):
            ll_as_array.append(self.data)
            self = self.next
        ll_reversed = ListNode(ll_as_array[len(ll_as_array)-1])
        for i in reversed(range(len(ll_as_array)-1)):
            ll_reversed.addNode(ll_as_array[i])
        return ll_reversed
