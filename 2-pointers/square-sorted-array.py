# program to square non-descreasing sorted array.
# logic : 1. separate the +ve and -ve parts of the array. 
# 2. check if either of them is empty. if all +ve simply square it and return, and if all -ve array, square and reverse it then return.  
# 3. if both +ve and -ve exists. square both parts and reverse the -ve array. now both will be in non-decreasing order. 
# 4. final step merge them and return. 

arr = [-4, -1, 0, 2, 6]

def square_array(arr):

    pos = []
    neg = []

    for i in arr:                   
        if i >= 0:
            pos.append(i)

        else: 
            neg.append(i)

    squared_pos = [a*a for a in pos]
    squared_neg = [a*a for a in neg]

    if not neg:        # all +ve


        return squared_pos                    

    if not pos:              # all -ve
          

        return squared_neg

    squared_neg = squared_neg[::-1]

    # at this point both -ve and +ve elements exists 
    # now merge it 

    k = len(squared_pos)
    m = len(squared_neg)

    i = 0      # for k, +ve array 
    j = 0      # for m, -ve array
    res = []

    while i < k and j < m:
        if squared_pos[i] <= squared_neg[j]:
            res.append(squared_pos[i])

            i += 1

        else: 
            res.append(squared_neg[j])

            j += 1
 
    res.extend(squared_pos[i: : ])            
    res.extend(squared_neg[j: : ])

    return res            


print(square_array(arr))