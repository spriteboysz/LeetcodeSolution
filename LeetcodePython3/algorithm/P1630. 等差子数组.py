#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:38
FileName: algorithm/P1630. 等差子数组.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(left, right):
            arr = sorted(nums[left:right + 1])
            return len(set([d2 - d1 for d1, d2 in pairwise(arr)])) == 1

        return [check(a, b) for a, b in zip(l, r)]


if __name__ == '__main__':
    solution = Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5])
    print('<None>' if solution is None else f'{solution=}')
