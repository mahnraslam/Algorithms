 
#Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue.
#Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

#FUNCTIONS
# getSize()– Get the number of items in the stack.
# isEmpty() – print( True if the stack is empty, False otherwise
#Peek() - print( top element in stack
# push(value) – Push a value into the top of the stack.
# pop() – Remove and print( a value in the top of the stack. If the stack is empty, raise an exception.

# First by using Array of fixed size .For Dyanamic create double size array when array is filled
class Stack:
    def __init__(self, size=100):
        self.array = [None]*size
        self.size  = size - 1
        self.top  = 0
    def getSize(self):
        print(self.top)
    
    def isEmpty(self):
        print(self.top == 0)
    
    def peek(self):
        print(self.array[self.top])
    def push(self,value):
        if self.top+1 > self.size :
            print( f"Stack is already filled")
        else :
            self.array[self.top] = value
            self.top += 1

    def pop(self):
        if self.top==0:
            print( f"Stack is empty")
        else :
            value = self.array[self.top-1] 
            self.array[self.top] = None
            self.top -= 1
            print(value)
        
if __name__=="__main__":
    obj = Stack(5)
    obj.push(2)
    obj.push(1)
    obj.push(3)
    obj.push(5)
    obj.push(5)
    obj.pop()
 
#Using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack2:
    def __init__(self):
        self.top = None
        self.size = 0

    def getSize(self):
        print(self.size)
    
    def isEmpty(self):
        print(self.size == 0)
    
    def peek(self):
        return self.top

    def pop(self):
        if self.isEmpty():
            return "Stack empty"
        else:
            tmp = self.top
            self.top = tmp.next
            self.size -= 1
            tmp.next = None
            return tmp.data
    def pop(self):
        if self.isEmpty():
            return "Stack empty"
        else:
            tmp = self.top
            self.top =  tmp.next
            self.size -= 1
            tmp.next = None
            return tmp.data
    def push(self,value):
        if self.size == 0:
            self.top = Node(value)
        else :
            cur = self.top
            self.top = Node(value)
            self.top.next = cur
        self.size += 1

    
    
        
        
