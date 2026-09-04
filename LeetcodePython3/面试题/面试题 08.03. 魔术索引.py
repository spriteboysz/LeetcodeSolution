#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:20
FileName: 面试题/面试题 08.03. 魔术索引.py
Description: 
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findMagicIndex(nums=[0, 2, 3, 4, 5])
    print(solution)
