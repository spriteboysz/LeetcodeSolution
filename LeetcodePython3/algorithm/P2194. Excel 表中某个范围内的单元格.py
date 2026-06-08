#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:06
FileName: P2194. Excel 表中某个范围内的单元格.py
Description:
"""
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a1, b1, _, a2, b2 = s
        cells = []
        for a in range(ord(a1), ord(a2) + 1):
            for b in range(int(b1), int(b2) + 1):
                cells.append(f'{chr(a)}{b}')
        return cells


if __name__ == '__main__':
    solution = Solution().cellsInRange(s="K1:L2")
    print(solution)
