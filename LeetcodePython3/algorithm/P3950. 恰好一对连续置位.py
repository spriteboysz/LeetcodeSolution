#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:50
FileName: P3950. 恰好一对连续置位.py
Description:
"""
from itertools import pairwise


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        return sum(ch1 + ch2 == '11' for ch1, ch2 in pairwise(bin(n)[2:])) == 1


if __name__ == '__main__':
    solution = Solution().consecutiveSetBits(6)
    print(solution)
