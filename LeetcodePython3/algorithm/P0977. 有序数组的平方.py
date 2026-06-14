#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:53
FileName: P0977. 有序数组的平方.py
Description:
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])


if __name__ == '__main__':
    solution = Solution().sortedSquares(nums=[-7, -3, 2, 3, 11])
    print(solution)
