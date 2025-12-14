#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 23:04
FileName: P3718. 缺失的最小倍数.py
Description:
"""
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        for i in range(1, 102):
            if k * i not in seen:
                return k * i
        return -1


if __name__ == '__main__':
    s = Solution().missingMultiple(nums=[8, 2, 3, 4, 6], k=2)
    print(s)
