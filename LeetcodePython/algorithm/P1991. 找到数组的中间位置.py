#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:09
FileName: algorithm/P1991. 找到数组的中间位置.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ss, acc = sum(nums), 0
        for i, num in enumerate(nums):
            if acc * 2 == ss - num:
                return i
            acc += num
        return -1


if __name__ == '__main__':
    solution = Solution().findMiddleIndex(nums=[2, 3, -1, 8, 4])
    ic(solution)
