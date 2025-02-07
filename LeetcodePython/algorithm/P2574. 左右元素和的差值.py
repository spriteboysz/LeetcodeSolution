#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:37
FileName: P2574. 左右元素和的差值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right, diff = 0, sum(nums), []
        for num in nums:
            right -= num
            diff.append(abs(left - right))
            left += num
        return diff


if __name__ == '__main__':
    solution = Solution().leftRightDifference(nums=[10, 4, 8, 3])
    ic(solution)
