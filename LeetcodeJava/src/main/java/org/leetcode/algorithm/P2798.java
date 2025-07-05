package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-06-23 23:43
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 2798. 满足目标工作时长的员工数目
 */

public class P2798 {
    class Solution {
        public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
            int cnt = 0;
            for (int hour : hours) {
                if (hour >= target) {
                    cnt += 1;
                }
            }
            return cnt;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2798().new Solution();
        Object ans = s.numberOfEmployeesWhoMetTarget(new int[]{0, 1, 2, 3, 4}, 2);
        System.out.println(ans);
    }
}
