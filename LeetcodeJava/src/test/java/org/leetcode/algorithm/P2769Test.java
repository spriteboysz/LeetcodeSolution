package org.leetcode.algorithm;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class P2769Test {

    @Test
    void test_001() {
        P2769.Solution s = new P2769().new Solution();
        int ans = s.theMaximumAchievableX(4, 1);
        System.out.println(ans);
        assertEquals(6, ans);
    }
}