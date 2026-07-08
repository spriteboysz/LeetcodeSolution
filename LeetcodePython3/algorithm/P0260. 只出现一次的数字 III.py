#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:21
FileName: P0260. 只出现一次的数字 III.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, cnt in counter.items() if cnt == 1]


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[1, 2, 1, 3, 2, 5])
    print(solution)
