#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-18 23:07
FileName: P0806. 写字符串需要的行数.py
Description:
"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row, column = 0, 0
        for ch in s:
            width = widths[ord(ch) - ord('a')]
            if column + width > 100:
                row += 1
                column = width
            else:
                column += width
        return [row + 1 if column > 0 else row, column]


if __name__ == '__main__':
    solution = Solution().numberOfLines(
        widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        s="bbbcccdddaaa"
    )
    print(solution)
