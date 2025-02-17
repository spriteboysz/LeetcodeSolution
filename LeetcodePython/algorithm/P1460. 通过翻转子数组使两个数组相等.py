#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 23:13
FileName: P1460. 通过翻转子数组使两个数组相等
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


if __name__ == '__main__':
    solution = Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3])
    ic(solution)
