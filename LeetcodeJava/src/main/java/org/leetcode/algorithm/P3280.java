package org.leetcode.algorithm;

/**
 * Author: Deean
 * Date: 2025-03-09 10:39
 * FileName: src/main/java/org/leetcode/algorithm
 * Description:
 */

public class P3280 {
    class Solution {
        public String convertDateToBinary(String date) {
            String[] nums = date.split("-");
            for (int i = 0; i < nums.length; i++) {
                nums[i] = Integer.toBinaryString(Integer.parseInt(nums[i]));
            }
            return String.join("-", nums);
        }
    }

    public static void main(String[] args) {
        Solution s = new P3280().new Solution();
        Object ans = s.convertDateToBinary("2080-02-09");
        System.out.println(ans);
    }
}
