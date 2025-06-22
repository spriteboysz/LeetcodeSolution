package org.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * Author: Deean
 * Date: 2025-06-22 11:48
 * FileName: src/main/java/org/leetcode/algorithm
 * Description:
 */

public class P2942 {
    class Solution {
        public List<Integer> findWordsContaining(String[] words, char x) {
            List<Integer> index = new ArrayList<>();
            for (int i = 0; i < words.length; i++) {
                if (words[i].indexOf(x) >= 0) {
                    index.add(i);
                }
            }
            return index;
        }
    }

    public static void main(String[] args) {
        Solution s = new P2942().new Solution();
        Object ans = s.findWordsContaining(new String[]{"leet", "code"}, 'e');
        System.out.println(ans);
    }
}
