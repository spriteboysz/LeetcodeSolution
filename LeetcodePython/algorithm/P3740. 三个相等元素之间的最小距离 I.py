#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 22:04
FileName: P3740. 三个相等元素之间的最小距离 I.py
Description:
"""
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        counters = defaultdict(list)
        for i, num in enumerate(nums):
            counters[num].append(i)
        minimum = inf
        for counter in counters.values():
            if len(counter) < 3:
                continue
            for i in range(len(counter) - 3 + 1):
                val = 2 * (counter[i + 2] - counter[i])
                minimum = min(minimum, val)
        return minimum if minimum != inf else -1


if __name__ == '__main__':
    s = Solution().minimumDistance(nums=[1, 1, 2, 3, 2, 1, 2])
    print(s)
