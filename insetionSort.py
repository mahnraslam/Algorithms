#Best case : When elements in acending order
# worst case : when elements in decending order .Slower than selection sort 1/2 N2 
#No of exchanges equals to number of inversion
import time

def insertionSort(array):
    s = time.time()
    for i in range(1, len(array)):          #Start from second element then compare it to previous.
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:    # Loop will continue until it will be larger from the previous
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    print("Time taken:", time.time() - s)
    return array

# Test the function 
array = [3,5,236,4,1,2,321,23,435423,545,132,65,76,89767,234,673,7656,2346,9765,53233,66,2,2,56,678 ]
array2 = ["a","h","z","b","i","o","t","w"]
print(insertionSort(array2)) 

