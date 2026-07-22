#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-21 23:51
FileName: P0888. 公平的糖果交换.py
Description:
"""
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1, sum2 = sum(aliceSizes), sum(bobSizes)
        diff = sum1 - (sum1 + sum2) // 2
        for a in aliceSizes:
            for b in bobSizes:
                if a - b == diff:
                    return [a, b]
        raise ValueError()


if __name__ == '__main__':
    solution = Solution().fairCandySwap(aliceSizes=[1, 2, 5], bobSizes=[2, 4])
    print(solution)
