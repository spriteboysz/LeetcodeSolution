#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 13:11
FileName: P2778. 特殊元素平方和
Description:
"""
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([num * num for i, num in enumerate(nums) if len(nums) % (i + 1) == 0])


if __name__ == '__main__':
    solution = Solution().sumOfSquares(nums=[2, 7, 1, 19, 18, 3])
    print(solution)
