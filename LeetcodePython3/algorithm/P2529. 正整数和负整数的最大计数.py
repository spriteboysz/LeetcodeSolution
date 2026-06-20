#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:32
FileName: P2529. 正整数和负整数的最大计数.py
Description:
"""
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive, negative = 0, 0
        for num in nums:
            if num > 0:
                positive += 1
            if num < 0:
                negative += 1
        return max(positive, negative)


if __name__ == '__main__':
    solution = Solution().maximumCount(nums=[-2, -1, -1, 1, 2, 3])
    print(solution)
