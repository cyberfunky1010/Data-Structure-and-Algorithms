# remove duplicates from sorted array. 

# [1,1,1,2,2,2,3,3,3,3,4,4,4] - sorted array - return k = 4 & [1,2,3,4]

arr = [1,1,1,2,2,3,3,3,5]

def remove_duplicate(arr):

    if not arr:
        return 0
     
    write_idx = 0   # write pointer
    read_idx = 1    # read pointer

    n = len(arr)

    while read_idx < n:
        if arr[read_idx] != arr[write_idx]:    # checks for unique elements 
           write_idx += 1
           arr[write_idx] = arr[read_idx]     # write unique elements

        read_idx += 1           # if duplicate just duplicate

    return write_idx + 1             # length is index + 1


print( remove_duplicate(arr))

