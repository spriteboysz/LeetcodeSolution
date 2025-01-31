#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:07
FileName: P1523. 在区间范围内统计奇数数目
Description:
"""

from icecream import ic


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1


if __name__ == '__main__':
    solution = Solution().countOdds(3, 7)
    ic(solution)
