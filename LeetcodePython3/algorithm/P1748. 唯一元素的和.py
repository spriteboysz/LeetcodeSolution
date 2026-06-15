#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:33
FileName: P1748. 唯一元素的和.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num in nums if Counter(nums).get(num, 0) == 1)


if __name__ == '__main__':
    solution = Solution().sumOfUnique(nums=[1, 2, 3, 2])
    print(solution)
