package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-23 23:27
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 3516. 找到最近的人
 */

public class P3516 {
    class Solution {
        public int findClosest(int x, int y, int z) {
            int t1 = Math.abs(x - z);
            int t2 = Math.abs(y - z);
            if (t1 == t2) {
                return 0;
            }
            return t1 < t2 ? 1 : 2;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3516().new Solution();
        Object ans = s.findClosest(2, 7, 4);
        System.out.println(ans);
    }
}
