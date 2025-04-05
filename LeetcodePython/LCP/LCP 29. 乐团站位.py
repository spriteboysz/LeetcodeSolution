#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 12:59
FileName: LCP/LCP 29. 乐团站位.py
Description: 
"""

from icecream import ic


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        x, y = xPos + 1, yPos + 1
        q = min(x, y, num - x + 1, num - y + 1)
        if x == y == q:
            nums = 1
        elif y > x:
            nums = y + x - 2 * q + 1
        else:
            nums = 4 * (num - 2 * q + 1) - (x + y - 2 * q) + 1
        count = 2 * ((num - 1) + (num - 2 * (q - 1) + 1)) * (q - 1) + nums
        return 9 if count % 9 == 0 else count % 9


if __name__ == '__main__':
    solution = Solution().orchestraLayout(4, 1, 2)
    ic(solution)
