#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 12:08
FileName: P3046. 分割数组
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) <= 2


if __name__ == '__main__':
    solution = Solution().isPossibleToSplit([1, 1, 2, 2, 3, 4])
    ic(solution)
