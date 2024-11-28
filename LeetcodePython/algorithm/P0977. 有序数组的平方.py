#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 23:11
FileName: P977. 有序数组的平方
Description:
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=abs)
        return [num ** 2 for num in nums]


if __name__ == '__main__':
    solution = Solution().sortedSquares(nums=[-4, -1, 0, 3, 10])
    print(solution)
