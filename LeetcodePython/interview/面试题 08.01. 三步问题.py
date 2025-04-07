#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 23:05
FileName: interview/面试题 08.01. 三步问题.py
Description: 
"""

from icecream import ic


class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0, 1, 2, 4]
        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % (10 ** 9 + 7))
        return dp[n]


if __name__ == '__main__':
    solution = Solution().waysToStep(5)
    ic(solution)
