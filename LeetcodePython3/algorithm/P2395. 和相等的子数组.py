#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 10:09
FileName: P2395. 和相等的子数组.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        pairs = [sum(pair) for pair in pairwise(nums)]
        return len(pairs) > len(set(pairs))


if __name__ == '__main__':
    solution = Solution().findSubarrays(nums=[4, 2, 4])
    print(solution)
