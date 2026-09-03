#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 23:06
FileName: LC/LC 06. 拿硬币.py
Description: 
"""
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin + 1) // 2 for coin in coins)


if __name__ == '__main__':
    solution = Solution().minCount([4, 2, 1])
    print(solution)
