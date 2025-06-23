package org.leetcode.algorithm;

import java.util.Arrays;

/**
 * Author: Deean
 * Date: 2025-06-23 23:31
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 2545. 根据第 K 场考试的分数排序
 */

public class P2545 {
    class Solution {
        public int[][] sortTheStudents(int[][] score, int k) {
            Arrays.sort(score, (u, v) -> v[k] - u[k]);
            return score;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2545().new Solution();
        Object ans = s.sortTheStudents(new int[][]{{10, 6, 9, 1}, {7, 5, 11, 2}, {4, 8, 3, 15}}, 2);
        System.out.println(ans);
    }
}
