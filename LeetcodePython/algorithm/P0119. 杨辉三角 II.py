#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-02 22:44
FileName: P0119. 杨辉三角 II
Description:
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1, *[num1 + num2 for num1, num2 in zip(row, row[1:])], 1]
        return row


if __name__ == '__main__':
    solution = Solution().getRow(5)
    print(solution)
