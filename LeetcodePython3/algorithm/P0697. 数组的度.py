#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 11:40
FileName: P0697. 数组的度.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        degree = max(len(v) for v in dic.values())
        return min(v[-1] - v[0] + 1 for v in dic.values() if len(v) == degree)


if __name__ == '__main__':
    solution = Solution().findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2])
    print(solution)
