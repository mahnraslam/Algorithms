# For first iteraion i= 0 or first index
# smallest :0 and element  set to a[smallest] = a[0] 
# check the whole array afetr a[0] and change the smallest to  5 and replace a[0] to a[5]
# For second  iteraion i=1  
# smallest :1  and element  set to a[smallest] = a[1] 
# check the whole array after a[1] and change the smallest to 7 and replace a[1] to a[7] and so on
  
# When elements in decending order ,selection sort is better than insertion sort. 
# The number of compares and exchanges made by selection sort does not depend on the order of the input.
def selectionSort(a):

    for i in range(len( a)):
        smallest =  i
        for j in range(i+1, len(a)): 
            if a[j] < a[smallest] : #Check smallest number after the i th  index 
                smallest =  j

        #swaps if i not equal to smallest 
        if i != smallest :
            a[i], a[smallest] =  a[smallest], a[i]
    return a

a = [5,4,3,5,26,2,7,2]
print(selectionSort(a))
 