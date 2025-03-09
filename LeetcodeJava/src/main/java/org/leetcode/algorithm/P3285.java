package org.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * Author: Deean
 * Date: 2025-03-09 10:21
 * FileName: src/main/java/org/leetcode/algorithm
 * Description: 3285. 找到稳定山的下标
 */

public class P3285 {
    class Solution {
        public List<Integer> stableMountains(int[] height, int threshold) {
            List<Integer> mountains = new ArrayList<>();
            for (int i = 1; i < height.length; i++) {
                if (height[i - 1] > threshold) {
                    mountains.add(i);
                }
            }
            return mountains;
        }
    }

    public static void main(String[] args) {
        Solution s = new P3285().new Solution();
        Object ans = s.stableMountains(new int[]{1, 2, 3, 4, 5}, 2);
        System.out.println(ans);
    }
}
