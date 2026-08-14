#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-11 22:54
FileName: P3740. 三个相等元素之间的最小距离 I.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        counters = defaultdict(list)
        for i, num in enumerate(nums):
            counters[num].append(i)
        minimum = len(nums) * 3
        for counter in counters.values():
            if len(counter) < 3:
                continue
            for i in range(len(counter) - 3 + 1):
                a, b, c = counter[i:i + 3]
                val = c + c - a - a
                minimum = min(minimum, val)
        return minimum if minimum != len(nums) * 3 else -1


if __name__ == '__main__':
    solution = Solution().minimumDistance(nums=[1, 1, 2, 3, 2, 1, 2])
    print(solution)
