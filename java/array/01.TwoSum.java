
// Link --> https://leetcode.com/problems/two-sum/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            result = target - nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                if (result == nums[j]) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}