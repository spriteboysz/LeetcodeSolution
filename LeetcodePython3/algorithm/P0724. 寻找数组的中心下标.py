#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:38
FileName: P0724. 寻找数组的中心下标.py
Description:
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, acc = sum(nums), 0
        for i, num in enumerate(nums):
            acc += num
            if acc * 2 == total + num:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
    print(solution)
