#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-13 18:29
FileName: algorithm/P1884. 鸡蛋掉落-两枚鸡蛋.py
Description: 
"""
from math import ceil, sqrt

from icecream import ic


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((sqrt(n * 8 + 1) - 1) / 2)


if __name__ == '__main__':
    solution = Solution().twoEggDrop(100)
    ic(solution)
