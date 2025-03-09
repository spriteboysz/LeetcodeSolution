package org.leetcode.algorithm;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class P3285Test {

    @Test
    void test_001() {
        P3285.Solution s = new P3285().new Solution();
        List<Integer> ans = s.stableMountains(new int[]{1, 2, 3, 4, 5}, 2);
        List<Integer> expect = Arrays.asList(3, 4);
        assertEquals(expect, ans);
    }
}