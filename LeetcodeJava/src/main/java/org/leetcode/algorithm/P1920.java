package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-23 23:50
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 1920. 基于排列构建数组
 */

public class P1920 {
    class Solution {
        public int[] buildArray(int[] nums) {
            int[] ans = new int[nums.length];
            for (int i = 0; i < nums.length; ++i) {
                ans[i] = nums[nums[i]];
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution s = new P1920().new Solution();
        Object ans = s.buildArray(new int[]{0, 2, 1, 5, 3, 4});
        System.out.println(ans.toString());
    }
}
