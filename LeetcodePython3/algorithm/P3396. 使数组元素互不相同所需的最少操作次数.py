#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 16:49
FileName: algorithm/P3396. 使数组元素互不相同所需的最少操作次数.py
Description: 
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumOperations(nums=[1, 2, 3, 4, 2, 3, 3, 5, 7])
    print('<None>' if solution is None else f'{solution=}')
