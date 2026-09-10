#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 13:27
FileName: 面试题/面试题 17.09. 第 k 个数.py
Description: 
"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [1] * (k + 1)
        i3, i5, i7 = 1, 1, 1
        for i in range(2, k + 1):
            curr = min(dp[i3] * 3, dp[i5] * 5, dp[i7] * 7)
            dp[i] = curr
            if curr == dp[i3] * 3:
                i3 += 1
            if curr == dp[i5] * 5:
                i5 += 1
            if curr == dp[i7] * 7:
                i7 += 1
        return dp[-1]


if __name__ == '__main__':
    solution = Solution().getKthMagicNumber(5)
    print('<None>' if not solution else f'{solution=}')
