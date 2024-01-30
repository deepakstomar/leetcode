
# Link -> 

from math import inf


def max_sub_array(nums):

    # negative infinite number
    max_sum = -inf
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0
    
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
# nums = [1]
# nums = [-1]

print(max_sub_array(nums))