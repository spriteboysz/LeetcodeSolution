#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:24
FileName: P1556. 千位分隔数.py
Description:
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        ss = str(n)[::-1]
        segments = [ss[i:i + 3] for i in range(0, len(ss), 3)]
        return '.'.join(segments)[::-1]


if __name__ == '__main__':
    solution = Solution().thousandSeparator(1234)
    print(solution)
