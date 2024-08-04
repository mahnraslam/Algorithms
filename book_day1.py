
import time 
# Time complexit will increase as input size increase
def sum(num):
    start_time = time.time()
    sum = 0
    for i in range(num+1):
        sum += i 
    end_time = time.time()
    return sum , end_time - start_time
print(sum(10**5))

#Efficient way 
#  First, the times recorded above are shorter than any of the previous examples.Second, they are very consistent no matter what the value of n. It appears that sumOfN3 is hardly impacted by the number of integers being added.
import time
def sum2(n):
    start_time = time.time()
    sum = (n*(n+1))/2
    return sum  ,  time.time() - start_time
print(sum2(10**10))