#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 19:43
FileName: P2206. 将数组划分成相等数对.py
Description:
"""
from typing import List, Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(v % 2 == 0 for v in counter.values())


if __name__ == '__main__':
    solution = Solution().divideArray(nums=[3, 2, 3, 2, 2, 2])
    print(solution)
