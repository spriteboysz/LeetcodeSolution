#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 16:59
FileName: LCR/LCR 180. 文件组合.py
Description: 
"""
import math
from typing import List

from icecream import ic


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        combination = []
        for start in range(1, target // 2 + 1):
            m = math.sqrt(2 * target - 2 * start + (2 * start + 1) ** 2 / 4) - (2 * start + 1) / 2
            if m == int(m):
                combination.append(list(range(start, start + int(m) + 1)))
        return combination


if __name__ == '__main__':
    solution = Solution().fileCombination(18)
    ic(solution)
