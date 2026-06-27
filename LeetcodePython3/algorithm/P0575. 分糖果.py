#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:08
FileName: P0575. 分糖果.py
Description:
"""
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


if __name__ == '__main__':
    solution = Solution().distributeCandies([1, 1, 2, 3])
    print(solution)
