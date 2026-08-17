# remove duplicates from sorted array. 

# [1,1,1,2,2,2,3,3,3,3,4,4,4] - sorted array - return k = 4 & [1,2,3,4]

arr = [1,1,1,2,2,3]

def remove_duplicate(arr):
     a = 0
     uniq = 1
     b = 1

     n = len(arr)

     while (b < n):
          if arr[b] == arr[b - 1]:
               b += 1

          arr[a + 1] = arr[a]

          a += 1
          b += 1
          uniq += 1

     return uniq


print( remove_duplicate(arr))

