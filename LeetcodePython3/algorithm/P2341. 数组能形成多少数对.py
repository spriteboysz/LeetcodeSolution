#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 10:04
FileName: P2341. 数组能形成多少数对.py
Description:
"""
from typing import List, Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [sum(cnt // 2 for cnt in counter.values()), sum(cnt % 2 for cnt in counter.values())]


if __name__ == '__main__':
    solution = Solution().numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2])
    print(solution)
