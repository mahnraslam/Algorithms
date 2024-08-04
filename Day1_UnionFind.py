from logging import raiseExceptions

class UnionFind:
    def __init__(self ,size = 10):
        if isinstance(size,int) and size>0 :
            self.__id = [i+1 for i in range(size)]
            self.__size = [1]*size
        else :
            raiseExceptions("size shoulb be a positive integer")
    def __str__(self):
        return f"{self.__id}"
    def root(self,num):
        if self.__id[num] == num:
            return num
        for i in self.__id :
            if num == self.__id[i]:
                return num
        return "Not a valid number"
    
    def connected(self,p,q):
        return  self.__id[p] == self.__id[q]

    def union(self,p,q):

        parent_p = self.root(p)
        parent_q = self.root(q)
        
        if self.__size[p] > self.__size[q]:
            self.__id[parent_p-1] = parent_q
        else : 
            self.__id[parent_q-1] = parent_p

def main():
    obj1 = UnionFind()
    obj1.union(5,6)
    print(obj1.connected(5,6))
    print(obj1)
main()   
  