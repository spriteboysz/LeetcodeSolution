#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-04 21:11
FileName: P3880. 两个值之间的最小绝对差值.py
Description:
"""

from math import inf


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res = [inf] * 3
        for index, num in enumerate(nums):
            if num != 0:
                res[num] = index
            res[0] = min(res[0], abs(res[2] - res[1]))
        return int(res[0]) if res[0] != inf else -1


if __name__ == '__main__':
    solution = Solution().minAbsoluteDifference(nums=[1, 0, 0, 2, 0, 1])
    print(solution)
