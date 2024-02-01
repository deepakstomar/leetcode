class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxCapacity = 0;

        while(left < right) {
            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            int currentCapacity = width * minHeight;
            
            maxCapacity = Math.max(currentCapacity, maxCapacity);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxCapacity;
    }
}