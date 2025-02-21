#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-21 22:37
FileName: P2903. 找出满足差值条件的下标 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if abs(i - j) >= indexDifference and abs(num1 - num2) >= valueDifference:
                    return [i, j]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().findIndices(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4)
    ic(solution)
