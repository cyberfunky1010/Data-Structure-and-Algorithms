# triplet sum to zero. find all triplets that equals to 0. no duplicates allowed. 
# nums = [-1,0,1,2,-1,-4], sorted - [-4,-1,-1,0,1,2] output - [ [-1,-1,2], [-1,0,1] ]

nums = [-1,0,1,2,-1,-4]

def triplet_sum(nums):

    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-2):

        if nums[i] > 0: #array is sorted so if i > 0 then all elements coming after are all +ve. 3 +ve no.s can't be zero. so break.
            break

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, n-1

        target = -nums[i]                                              

        while left < right:

            s = nums[left] + nums[right]

            if s == target:

                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < target:
                
                left += 1
            else:
                right -= 1


    return result                    



res = triplet_sum(nums)

print(res)