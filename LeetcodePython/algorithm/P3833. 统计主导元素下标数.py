#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-02-28 22:30
FileName: P3833. 统计主导元素下标数.py
Description:
"""
from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        acc, count = sum(nums), 0
        for i, num in enumerate(nums[:-1]):
            acc = acc - num
            if num > acc / (len(nums) - 1 - i):
                count += 1
        return count


if __name__ == '__main__':
    s = Solution().dominantIndices([5, 4, 3])
    print(s)
