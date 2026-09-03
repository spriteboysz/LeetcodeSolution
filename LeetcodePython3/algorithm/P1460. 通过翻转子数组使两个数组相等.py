#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:42
FileName: algorithm/P1460. 通过翻转子数组使两个数组相等.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == '__main__':
    solution = Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3])
    print(solution)
