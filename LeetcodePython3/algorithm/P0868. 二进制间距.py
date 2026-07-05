#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 11:48
FileName: P0868. 二进制间距.py
Description:
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        maximum, curr = 0, -1
        for i, ch in enumerate(bin(n)[2:]):
            if ch == '0':
                continue
            if curr != -1:
                maximum = max(i - curr, maximum)
            curr = i
        return maximum


if __name__ == '__main__':
    solution = Solution().binaryGap(22)
    print(solution)
