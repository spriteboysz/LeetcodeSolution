#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 16:13
FileName: algorithm/P3674. 数组元素相等的最小操作次数.py
Description: 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        return 1


if __name__ == '__main__':
    solution = Solution().minOperations([1, 2])
    print('<None>' if solution is None else f'{solution=}')
