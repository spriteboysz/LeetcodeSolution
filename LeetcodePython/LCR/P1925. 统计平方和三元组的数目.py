#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-07 23:38
FileName: LCR/P1925. 统计平方和三元组的数目.py
Description: 
"""

from icecream import ic


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                for c in range(max(a, b) + 1, n + 1):
                    if a * a + b * b == c * c:
                        # ic(a, b, c)
                        cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countTriples(10)
    ic(solution)
