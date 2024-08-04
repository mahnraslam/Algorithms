# #Using  Circular Queue
# Enqueue: Adds a new element to the queue.....self.rear+1%self.size
# Dequeue: Removes and returns the first (front) element from the queue.....self.rear-1%self.size
# Peek: Returns the first element in the queue....self.pop(0)
# isEmpty: Checks if the queue is empty.
# Size: Finds the number of elements in the queue.Size can be find if we make an other attribute that is called self.size 

# Using Linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, size = 100) :
        self.front = None 
        self.rear = None

    def  enqueue(self, value):
        if  self.isEmpty():
            self.rear = self.front = Node(value)
        tmp = self.rear
        self.rear = Node(value)
        self.rear.next = tmp
    
    def dequeue(self):

        if self.head==None:
            return 
        else:
            value = self.front
            self.front.next = self.front
            if self.front == None :
                self.rear = None
            return value
        
    def isEmpty(self):
        return self.front ==0 

