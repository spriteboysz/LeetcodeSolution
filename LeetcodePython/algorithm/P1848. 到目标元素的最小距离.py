#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:43
FileName: LCR/P1848. 到目标元素的最小距离.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, num in enumerate(nums) if num == target)


if __name__ == '__main__':
    solution = Solution().getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3)
    ic(solution)
