#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 20:24
FileName: algorithm/P2928. 给小朋友们分糖果 I.py
Description: 
"""

from icecream import ic


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cnt = 0
        for a in range(limit + 1):
            for b in range(limit + 1):
                c = n - a - b
                if 0 <= c <= limit:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().distributeCandies(3, 3)
    ic(solution)
