#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-10 23:04
FileName: P0006. Z 字形变换
Description:
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        grid = [[] for _ in range(numRows)]
        i, k = 0, -1
        for ch in s:
            grid[i].append(ch)
            if i == 0 or i == numRows - 1:
                k = -k
            i += k
        return ''.join([''.join(row) for row in grid])


if __name__ == '__main__':
    solution = Solution().convert(s="PAYPALISHIRING", numRows=4)
    print(solution)
