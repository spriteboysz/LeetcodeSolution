#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-09 21:34
FileName: P2161. 根据给定数字划分数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt = [num for num in nums if num < pivot]
        eq = [num for num in nums if num == pivot]
        gt = [num for num in nums if num > pivot]
        return lt + eq + gt


if __name__ == '__main__':
    solution = Solution().pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)
    ic(solution)
