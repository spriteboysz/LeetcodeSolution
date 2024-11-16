#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 08:48
FileName: P2643. 一最多的行
Description:
"""
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = [sum(row) for row in mat]
        maximum = max(rows)
        return [[i for i, el in enumerate(rows) if el == maximum][0], maximum]


if __name__ == '__main__':
    solution = Solution().rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]])
    print(solution)
