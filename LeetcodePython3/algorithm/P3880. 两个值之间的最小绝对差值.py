#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 23:16
FileName: P3880. 两个值之间的最小绝对差值.py
Description:
"""


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        index1 = [i for i, num in enumerate(nums) if num == 1]
        index2 = [i for i, num in enumerate(nums) if num == 2]
        return min((abs(i - j) for i in index1 for j in index2), default=-1)


if __name__ == '__main__':
    solution = Solution().minAbsoluteDifference(nums=[1, 0, 0, 2, 0, 1])
    print(solution)
