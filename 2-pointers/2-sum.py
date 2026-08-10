# two sum soted array. target = 9 so it should return index (1,2)

arr = [2,7,11,15]
target = 9

def two_sum(arr, target):

    i = 0
    j = len(arr) - 1

    while (i < j):

        sum = arr[i] + arr[j]

        if sum == target:
            return i+1,j+1

        elif sum < target:
            i = i + 1

        else:
            j = j - 1

print(two_sum(arr, target))