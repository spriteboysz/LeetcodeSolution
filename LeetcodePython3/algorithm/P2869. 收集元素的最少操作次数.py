#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 14:48
FileName: LC/P2869. 收集元素的最少操作次数.py
Description: 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen1, seen2 = set(), set(range(1, k + 1))
        for i, num in enumerate(nums[::-1]):
            seen1.add(num)
            if seen2 - seen1 == set():
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[3, 1, 5, 4, 2], k=2)
    print('<None>' if solution is None else f'{solution=}')
