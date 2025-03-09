package org.leetcode.algorithm;

import java.util.Arrays;

/**
 * Author: Deean
 * Date: 2025-03-09 13:19
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 2974. 最小数字游戏
 */

public class P2974 {
    class Solution {
        public int[] numberGame(int[] nums) {
            Arrays.sort(nums);
            for (int i = 0; i < nums.length; i += 2) {
                int num = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = num;
            }
            return nums;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2974().new Solution();
        Object ans = s.numberGame(new int[]{5, 4, 2, 3});
        System.out.println(Arrays.toString((int[]) ans));
    }
}
