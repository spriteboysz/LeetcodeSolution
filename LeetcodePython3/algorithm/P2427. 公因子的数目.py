#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:22
FileName: P2427. 公因子的数目.py
Description:
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int: 
        return sum(a % i == 0 and b % i == 0 for i in range(1, min(a, b) + 1))


if __name__ == '__main__':
    solution = Solution().commonFactors(25, 30)
    print(solution)
