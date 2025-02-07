#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:40
FileName: P2220. 转换数字的最少位翻转次数
Description:
"""

from icecream import ic


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()


if __name__ == '__main__':
    solution = Solution().minBitFlips(start=3, goal=4)
    ic(solution)
