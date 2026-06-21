#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:50
FileName: P3731. 找出缺失的元素.py
Description:
"""
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return sorted(set(range(min(nums), max(nums))) - set(nums))


if __name__ == '__main__':
    solution = Solution().findMissingElements([1, 4, 2, 5])
    print(solution)
