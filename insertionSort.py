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
    end = time.time()
    print("Time taken:", end- s)

    return array

# Test the function 
array = [3,5,236,4,1,2,321,23,435423,545,132,65,76,897,34,23432,454,676,3435,234,65456,65546,355454,343,234,673,7656,2346,9765,53233,66,
        2,2,56,678,3,5,236,4,1,2,321,23,435423,545,132,65,76,89767,234,673,7656,2346,9765,53233,66,2,2,56,678,
        3,5,236,4,1,2,321,23,435423,545,132,65,76,89767,234,673,7656,2346,9765,53233,66,2,2,56,678,4,5,3,5,2,65,6,45,65,334,23,76,8,87,56,98,67]
array2 = ["a","h","z","b","i","o","t","w"]
print(insertionSort(array)) 

