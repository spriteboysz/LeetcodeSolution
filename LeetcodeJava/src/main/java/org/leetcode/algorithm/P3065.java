package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-23 23:37
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 3065. 超过阈值的最少操作数 I
 */

public class P3065 {
    class Solution {
        public int minOperations(int[] nums, int k) {
            int cnt = 0;
            for (int num : nums) {
                if (num < k) {
                    cnt += 1;
                }
            }
            return cnt;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3065().new Solution();
        Object ans = s.minOperations(new int[]{2, 11, 10, 1, 3}, 10);
        System.out.println(ans);
    }
}
