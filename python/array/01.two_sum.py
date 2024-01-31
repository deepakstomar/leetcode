
# Link --> https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    nums_dict = {}
    n = len(nums)

    for i in range(n):
        difference = target - nums[i]
        if difference in nums_dict:
            return [nums_dict[difference], i]
        nums_dict[nums[i]] = i

nums = [2,3,5,6]
target = 7

print(two_sum(nums, target))