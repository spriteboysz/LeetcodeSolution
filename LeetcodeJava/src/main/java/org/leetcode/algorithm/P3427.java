package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-03-09 11:46
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 3427. 变长子数组求和
 */

public class P3427 {
    class Solution {
        public int subarraySum(int[] nums) {
            int sum = 0;
            for (int i = 0; i < nums.length; i++) {
                int start = Math.max(0, i - nums[i]);
                for (int j = start; j <= i; j++) {
                    sum += nums[j];
                }
            }
            return sum;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3427().new Solution();
        Object ans = s.subarraySum(new int[]{3, 1, 1, 2});
        System.out.println(ans);
    }
}
