# merge 2 non-descreasing sorted array.

arr1 = [2,4,5,7,8]
arr2 = [1,2,4,5,7,9]

def merge_sorted_array(arr1, arr2):
    n = len(arr1)    # length of arr1
    m = len(arr2)    # length of arr2 

    i = 0     # arr1 pointer
    j = 0     # arr2 pointer
    res = []

    while i < n and j < m: 
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1

        else: 

            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])    # adds the remaining of arr1. this line could also be written using while loop
    res.extend(arr2[j:])    # adds the remaining of arr2  but this is more pythonic way. 

    return res

a = merge_sorted_array(arr1, arr2)

print(a)
