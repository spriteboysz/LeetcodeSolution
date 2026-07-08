#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:25
FileName: P0347. 前 K 个高频元素.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(counter, key=lambda num: counter.get(num, 0), reverse=True)[:k]


if __name__ == '__main__':
    solution = Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
    print(solution)
