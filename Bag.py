#Bag via lnked ist
from typing import Generic, Optional, TypeVar
# Define a generic type variable T
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self,val:T ,next : Optional["Node[T]"] = None) -> None :
        self.value = val
        self.next = next 


# Bag class using a linked list   
class BagIterator:
    def __init__(self, data,size):
        self.current =  data
        self.linkedList_size  = size
        self.count = 0 

    def __next__( self ):
        if self.count < self.linkedList_size : 
            tmp = self.current 
            self.current = self.current.next
            self.count += 1
            return tmp.value
        else:
            raise StopIteration
    
 
class Bag(Generic[T]):
    def __init__(self) -> None:
        self.data : Optional[Node[T]]  = None
        self.size = 0

    def __iter__(self): 
        return BagIterator(self.data,self.size)
    
    def add(self,item):
        new_node = Node(item)
        if not self.data :
            self.data  = new_node 
        else : 
            cur = self.data
            while cur.next != None :
                cur = cur.next 
            cur.next = Node(item)
            self.size += 1



    def remove(self, num: int) -> None:
        if num <= 0 or num > self.size:
            print(f"Invalid item number")
            return

        cur = self.data
        if num == 1:
            self.data = self.data.next
        else:
            for _ in range(1, num - 1):
                cur = cur.next
            tmp = cur.next
            cur.next = tmp.next
            print(f"Removed: {tmp.value}")

        self.size -= 1

if __name__ == "__main__":
    b = Bag[int]()
    b.add(14)
    b.add(45)
    b.add(56)
    b.add(87)
    b.remove(1)
    b.remove(1)
    b.remove(1)

    print("Loop starts")
    for item in b:
        print(f"Element: {item}")
