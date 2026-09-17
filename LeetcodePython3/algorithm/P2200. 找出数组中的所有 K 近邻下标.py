#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 14:02
FileName: algorithm/P2200. 找出数组中的所有 K 近邻下标.py
Description: 
"""
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexes = set()
        for i, num in enumerate(nums):
            if num == key:
                left = max(0, i - k)
                right = min(len(nums), i + k + 1)
                indexes.update(range(left, right))
        return sorted(indexes)


if __name__ == '__main__':
    solution = Solution().findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1)
    print('<None>' if solution is None else f'{solution=}')
