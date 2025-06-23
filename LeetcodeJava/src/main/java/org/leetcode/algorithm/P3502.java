package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-22 12:13
 * FileName: src/main/java/org/leetcode/algorithm
 * Description:
 */

public class P3502 {
    class Solution {
        public int[] minCosts(int[] cost) {
            int[] ans = new int[cost.length];
            int minimum = cost[0];
            for (int i = 0; i < cost.length; i++) {
                minimum = Math.min(minimum, cost[i]);
                ans[i] = minimum;
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3502().new Solution();
        Object ans = s.minCosts(new int[]{5, 3, 4, 1, 3, 2});
        System.out.println(ans.toString());
    }
}
