#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 10:46
FileName: algorithm/P0441. 排列硬币.py
Description: 
"""

import math
from icecream import ic


class Solution:
    def arrangeCoins(self, n: int) -> int:
        discriminant = 1 + 8 * n
        return int((math.sqrt(discriminant) - 1) // 2)


if __name__ == '__main__':
    solution = Solution().arrangeCoins(8)
    ic(solution)
