#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 18:30
FileName: P0119. 杨辉三角 II.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        for _ in range(rowIndex):
            row = [1, *[a + b for a, b in pairwise(row)], 1]
        return row


if __name__ == '__main__':
    solution = Solution().getRow(1)
    print(solution)
