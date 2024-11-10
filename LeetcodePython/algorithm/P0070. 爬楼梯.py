#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:11
FileName: P0070. 爬楼梯
Description:
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution().climbStairs(3)
    print(solution)
