#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 21:34
FileName: algorithm/P1608. 特殊数组的特征值.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(num >= x for num in nums) == x:
                return x
        return -1


if __name__ == '__main__':
    solution = Solution().specialArray(nums=[3, 5])
    ic(solution)
    solution = Solution().specialArray(nums=[0, 4, 3, 0, 4])
    ic(solution)
