package org.leetcode.algorithm;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class P3110Test {
    @Test
    void test_001() {
        P3110.Solution s = new P3110().new Solution();
        int ans = s.scoreOfString("hello");
        System.out.println(ans);
        assertEquals(13, ans);
    }

}