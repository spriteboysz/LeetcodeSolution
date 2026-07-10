#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:03
FileName: P3370. 仅含置位位的最小整数.py
Description:
"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(bin(n).replace('0', '1')[2:], 2)


if __name__ == '__main__':
    solution = Solution().smallestNumber(10)
    print(solution)
