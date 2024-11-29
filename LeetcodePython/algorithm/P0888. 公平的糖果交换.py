#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 22:40
FileName: P0888. 公平的糖果交换
Description:
"""
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1, sum2 = sum(aliceSizes), sum(bobSizes)
        diff1 = (sum1 + sum2) // 2 - sum1
        seen = set(bobSizes)
        for size in aliceSizes:
            if size + diff1 in seen:
                return [size, size + diff1]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().fairCandySwap(aliceSizes=[1, 2, 5], bobSizes=[2, 4])
    print(solution)
