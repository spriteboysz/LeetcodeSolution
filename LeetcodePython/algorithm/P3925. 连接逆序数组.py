#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-17 08:58
FileName: P3925. 连接逆序数组.py
Description:
"""


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]


if __name__ == '__main__':
    solution = Solution().concatWithReverse(nums=[1, 2, 3])
    print(solution)
