#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-27 22:28
FileName: algorithm/P0806. 写字符串需要的行数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        rows, curr = 0, 0
        for ch in s:
            width = widths[ord(ch) - ord('a')]
            if curr + width > 100:
                rows += 1
                curr = width
            else:
                curr += width
        return [rows + 1, curr]


if __name__ == '__main__':
    solution = Solution().numberOfLines(
        widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        s="abcdefghijklmnopqrstuvwxyz")
    ic(solution)
