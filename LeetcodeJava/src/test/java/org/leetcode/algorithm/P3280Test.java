package org.leetcode.algorithm;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class P3280Test {

    @Test
    void test_001() {
        P3280.Solution s = new P3280().new Solution();
        String ans = s.convertDateToBinary("2080-02-09");
        assertEquals("100000100000-10-1001", ans);
    }
}