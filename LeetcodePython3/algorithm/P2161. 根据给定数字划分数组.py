#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 23:29
FileName: LCP/P2161. 根据给定数字划分数组.py
Description: 
"""
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [num for num in nums if num < pivot]
        middle = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        return left + middle + right


if __name__ == '__main__':
    solution = Solution().pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)
    print(solution)
