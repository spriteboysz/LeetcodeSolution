#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 16:16
FileName: P0624. 数组列表中的最大距离.py
Description:
"""

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maximum = min(array[0] for array in arrays) - 1
        minimum = max(array[-1] for array in arrays) + 1
        ans = 0
        for array in arrays:
            ans = max(ans, array[-1] - minimum, maximum - array[0])
            minimum = min(minimum, array[0])
            maximum = max(maximum, array[-1])
        return ans


if __name__ == '__main__':
    solution = Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]])
    print(solution)
