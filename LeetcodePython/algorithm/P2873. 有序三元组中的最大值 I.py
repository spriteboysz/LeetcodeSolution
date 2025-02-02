#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 23:14
FileName: P2873. 有序三元组中的最大值 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum = -1
        for k, num3 in enumerate(nums):
            for j, num2 in enumerate(nums[:k]):
                for i, num1 in enumerate(nums[:j]):
                    maximum = max(maximum, (num1 - num2) * num3)
        return max(0, maximum)


if __name__ == '__main__':
    solution = Solution().maximumTripletValue(nums=[12, 6, 1, 2, 7])
    ic(solution)
