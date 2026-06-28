#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:24
FileName: P2784. 检查数组是否是好的.py
Description:
"""
from typing import List, Counter


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        return Counter((*range(1, n), n - 1)) == Counter(nums)


if __name__ == '__main__':
    solution = Solution().isGood([1, 3, 3, 2])
    print(solution)
