#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:22
FileName: P0191. 位1的个数.py
Description:
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


if __name__ == '__main__':
    solution = Solution().hammingWeight(n=2147483645)
    print(solution)
