a = [2,3,2,1]
b = [1,2,3,2]
print(a==b,sorted(a)==sorted(b))

def isPermutation(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    return (arr1 != arr2) and (sorted(arr1)== sorted(arr2))
 
def intersection_in_sorted_lists(arr1,arr2):
    j = 0
    res = {}
    while  i < len(arr1) and j < len(arr2) :
        if arr1[i] > arr2[j]  :
            j += 1
        elif arr1[i] < arr2[j] :
            i += 1
        else:
            res.add(arr1[i])
            i += 1
            j += 1
            
