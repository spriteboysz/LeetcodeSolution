#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-06 23:25
FileName: P2656. K 个元素的最大和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        return sum(range(maximum, maximum + k))


if __name__ == '__main__':
    solution = Solution().maximizeSum(nums=[1, 2, 3, 4, 5], k=3)
    ic(solution)
