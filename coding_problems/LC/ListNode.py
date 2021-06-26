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