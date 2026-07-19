#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:28
FileName: P0070. 爬楼梯.py
Description:
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0, 1, 2]
        for _ in range(2, n):
            stairs.append(stairs[-1] + stairs[-2])
        return stairs[n]


if __name__ == '__main__':
    solution = Solution().climbStairs(3)
    print(solution)
