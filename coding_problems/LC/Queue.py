# code copied by hand from: https://www.geeksforgeeks.org/queue-linked-list-implementation/
# queue is FIFO, first in first out
class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# A class to represent a queue
  
# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None    # return stack as string
    def isEmpty(self):
        return self.front == None
    # add an item to the queue
    def EnQueue(self,item):
        temp = QueueNode(item)
        # if we don't have a queue, create one with one node with the value passed in
        # otherwise add this to the back of the queue
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    def DeQueue(self):
        if self.isEmpty():
            return
        # remove the node at the front
        temp = self.front
        self.front = temp.next
        # if the queue has no front node, it has no rear node
        if self.front == None:
            self.rear = None

# driver code
if __name__ == "__main__":
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50) 
    q.DeQueue()   
    print("Queue Front " + str(q.front.val))
    print("Queue Rear " + str(q.rear.val))