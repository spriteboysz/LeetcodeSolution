#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 19:45
FileName: P2357. 使数组中所有元素都等于零.py
Description:
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})


if __name__ == '__main__':
    solution = Solution().minimumOperations(nums=[1, 5, 0, 3, 5])
    print(solution)
