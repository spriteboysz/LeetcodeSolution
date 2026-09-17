#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 13:48
FileName: algorithm/P1848. 到目标元素的最小距离.py
Description: 
"""
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distances = []
        for i, num in enumerate(nums):
            if num == target:
                distances.append(abs(i - start))
        return min(distances, default=0)


if __name__ == '__main__':
    solution = Solution().getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3)
    print('<None>' if solution is None else f'{solution=}')
