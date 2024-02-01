
# Link --> https://leetcode.com/problems/container-with-most-water/

def max_area(height):
    left = 0
    right = len(height) - 1
    max_capacity = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        current_capacity = min_height * width
        max_capacity = max(current_capacity, max_capacity)

        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1
    
    return max_capacity
    

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))

