package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-03-09 10:54
 * FileName: src/main/java/org/leetcode/algorithm
 * Description:
 */

public class P3110 {
    class Solution {
        public int scoreOfString(String s) {
            char[] ss = s.toCharArray();
            int score = 0;
            for (int i = 0; i < ss.length - 1; i++) {
                score += Math.abs(ss[i] - ss[i + 1]);
            }
            return score;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3110().new Solution();
        Object ans = s.scoreOfString("hello");
        System.out.println(ans);
    }
}
