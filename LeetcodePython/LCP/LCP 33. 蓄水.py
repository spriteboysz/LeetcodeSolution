#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-19 22:41
FileName: LCP 33. 蓄水.py
Description:
"""
from typing import List
from math import inf


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        maximum = max(vat)
        if maximum == 0:
            return 0
        ans = inf
        for x in range(1, maximum + 1):
            y = sum(max(0, (v + x - 1) // x - b) for v, b in zip(vat, bucket))
            ans = min(ans, x + y)
        return int(ans)


if __name__ == '__main__':
    solution = Solution().storeWater(bucket=[1, 3], vat=[6, 8])
    print(solution)
