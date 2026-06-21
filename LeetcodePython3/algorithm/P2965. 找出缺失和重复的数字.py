#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 15:30
FileName: P2965. 找出缺失和重复的数字.py
Description:
"""
from typing import List, Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num1, num2 = -1, -1
        counter = Counter(sum(grid, []))
        for num in range(1, len(grid) ** 2 + 1):
            if counter.get(num, 0) == 2:
                num1 = num
            if counter.get(num, 0) == 0:
                num2 = num
        return [num1, num2]


if __name__ == '__main__':
    solution = Solution().findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]])
    print(solution)
