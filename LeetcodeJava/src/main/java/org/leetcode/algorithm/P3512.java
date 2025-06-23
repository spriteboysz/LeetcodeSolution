package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-22 11:55
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 3512. 使数组和能被 K 整除的最少操作次数
 */

public class P3512 {
    class Solution {
        public int minOperations(int[] nums, int k) {
            int sum = 0;
            for (int num : nums) {
                sum += num;
            }
            return sum % k;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3512().new Solution();
        Object ans = s.minOperations(new int[]{3, 9, 7}, 5);
        System.out.println(ans);
    }
}
