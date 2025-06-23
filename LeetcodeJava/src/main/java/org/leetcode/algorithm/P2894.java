package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-23 23:22
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 2894. 分类求和并作差
 */

public class P2894 {
    class Solution {
        public int differenceOfSums(int n, int m) {
            int sum = 0;
            for (int i = 1; i <= n; i++) {
                if (i % m != 0) {
                    sum += i;
                } else {
                    sum -= i;
                }
            }
            return sum;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2894().new Solution();
        Object ans = s.differenceOfSums(10, 3);
        System.out.println(ans);
    }
}
