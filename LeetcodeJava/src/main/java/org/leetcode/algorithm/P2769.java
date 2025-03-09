package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-03-09 10:05
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 2769. 找出最大的可达成数字
 */

public class P2769 {
    class Solution {
        public int theMaximumAchievableX(int num, int t) {
            return num + t * 2;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2769().new Solution();
        Object ans = s.theMaximumAchievableX(4, 1);
        System.out.println(ans);
    }
}
