# It is named after its inventor, Donald Shell, who introduced it in 1959.
# The algorithm uses a sequence of gaps (also known as the increment sequence)
# to determine the intervals over which to compare and sort elements

# i = 2: key = arr[2] (54). Compare with arr[0] (12). No swap needed.
# i = 3: key = arr[3] (2). Compare with arr[1] (34). Swap, making the array [12, 2, 54, 34, 3].
# i = 4: key = arr[4] (3). Compare with arr[2] (54). Swap, making the array [12, 2, 3, 34, 54].
import time

def shellSort(arr):
    gap  = len(arr)//2
    start = time.time()
    while gap>0 :  
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            # Put the key in its correct location
            arr[j] = key
        # Reduce the gap for the next element
        gap //= 2

    return arr,time.time() - start
# Test the function 
array =  [12, 34, 54, 2, 3]
array2 = [3,5,236,4,1,2,321,23,435423,545,132,65,76,897,34,23432,454,676,3435,234,65456,65546,355454,343,234,673,7656,2346,9765,53233,66,
        2,2,56,678,3,5,236,4,1,2,321,23,435423,545,132,65,76,89767,234,673,7656,2346,9765,53233,66,2,2,56,678,
        3,5,236,4,1,2,321,23,435423,545,132,65,76,89767,234,673,7656,2346,9765,53233,66,2,2,56,678,4,5,3,5,2,65,6,45,65,334,23,76,8,87,56,98,67]
print(shellSort(array)) 