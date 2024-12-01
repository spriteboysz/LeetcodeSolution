#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 19:37
FileName: P0461. 汉明距离
Description:
"""
from itertools import zip_longest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        for a, b in zip_longest(bin(x)[2:][::-1], bin(y)[2:][::-1], fillvalue='0'):
            if a != b:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().hammingDistance(1, 4)
    print(solution)
