package org.leetcode.algorithm;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class P3427Test {
    @Test
    void test_001() {
        P3427.Solution s = new P3427().new Solution();
        int ans = s.subarraySum(new int[]{3, 1, 1, 2});
        System.out.println(ans);
        assertEquals(13, ans);
    }
}