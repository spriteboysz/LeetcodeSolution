#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 11:48
FileName: P2733. 既不是最小值也不是最大值
Description:
"""
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        seen = list(set(nums) - {maximum} - {minimum})
        return seen[0] if seen else -1


if __name__ == '__main__':
    solution = Solution().findNonMinOrMax(nums=[3, 2, 1, 4])
    print(solution)
