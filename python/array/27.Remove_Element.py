
# Link -> https://leetcode.com/problems/remove-element/

from typing import List


def removeElement(nums: List[int], val: int) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index

nums = [3,2,2,3]
val = 3

# nums = [0,1,2,2,3,0,4,2]
# val = 2

print(removeElement(nums, val))