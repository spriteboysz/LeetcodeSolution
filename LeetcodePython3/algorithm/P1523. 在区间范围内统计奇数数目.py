#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:38
FileName: P1523. 在区间范围内统计奇数数目.py
Description:
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


if __name__ == '__main__':
    solution = Solution().countOdds(3, 7)
    print(solution)
