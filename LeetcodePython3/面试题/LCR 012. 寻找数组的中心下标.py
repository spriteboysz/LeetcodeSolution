#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 18:59
FileName: 面试题/LCR 012. 寻找数组的中心下标.py
Description: 
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc, total = 0, sum(nums)
        for i, num in enumerate(nums):
            if acc == total - num - acc:
                return i
            acc += num
        return -1


if __name__ == '__main__':
    solution = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
    print(solution)
