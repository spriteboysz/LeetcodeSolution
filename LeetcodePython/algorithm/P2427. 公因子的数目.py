#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 22:14
FileName: P2427. 公因子的数目
Description:
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum([a % i == 0 and b % i == 0 for i in range(1, min(a, b) + 1)])


if __name__ == '__main__':
    solution = Solution().commonFactors(12, 6)
    print(solution)
