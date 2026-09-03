#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:56
FileName: LC/LCR 133. 位 1 的个数.py
Description: 
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


if __name__ == '__main__':
    solution = Solution().hammingWeight(4294967293)
    print(solution)
