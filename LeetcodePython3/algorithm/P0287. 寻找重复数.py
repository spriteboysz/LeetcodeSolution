#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:52
FileName: algorithm/P0287. 寻找重复数.py
Description: 
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1


if __name__ == '__main__':
    solution = Solution().findDuplicate([1, 3, 4, 5, 4])
    print('<None>' if not solution else f'{solution=}')
