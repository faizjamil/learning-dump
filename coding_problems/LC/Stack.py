# code copied by hand from: https://www.geeksforgeeks.org/stack-in-python/
# stack is FILO, first in last out
class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = StackNode("head")
        self.size = 0
    # return stack as string
    def __str__(self) -> str:
        curr = self.head.next
        out = ""
        while curr:
            out += str(curr.val) + "->"
            curr = curr.next
        return out[:-3]
    def is_empty(self):
        return self.size == 0
    

    def get_size(self) -> int:
        return self.size
    # this simply gets the value of the top node
    def peek(self) -> int:
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        return self.head.next.val
    # adds new node with data passed in at top of stack
    def push(self, data: int):
        
        new_node = StackNode(data)
    
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1 
    # removes first node
    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.val
# driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1,11):
        stack.push(i)
    # string templating
    print(f"Stack: {stack}")
    for j in range(1,6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    