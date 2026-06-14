#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:27
FileName: P0905. 按奇偶排序数组.py
Description:
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda num: num % 2)


if __name__ == '__main__':
    solution = Solution().sortArrayByParity([1, 2, 3, 4])
    print(solution)
