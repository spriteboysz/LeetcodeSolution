#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:32
FileName: P0961. 在长度 2N 的数组中找出重复 N 次的元素.py
Description:
"""
from statistics import mode

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return mode(nums)


if __name__ == '__main__':
    solution = Solution().repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4])
    print(solution)
