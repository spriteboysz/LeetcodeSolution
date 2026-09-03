#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 16:06
FileName: LC/LCR 168. 丑数.py
Description: 
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        i2, i3, i5 = 1, 1, 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            num = min(num2, num3, num5)
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
            if num == num5:
                i5 += 1
            dp[i] = num
        return dp[n]


if __name__ == '__main__':
    solution = Solution().nthUglyNumber(10)
    print(solution)
