#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 15:01
FileName: algorithm/P3178. 找出 K 秒后拿着球的孩子.py
Description: 
"""


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        curr, direction = 0, 1
        while k:
            k -= 1
            curr += direction
            if curr == 0 or curr == n - 1:
                direction = -direction
        return curr


if __name__ == '__main__':
    solution = Solution().numberOfChild(3, 5)
    print('<None>' if solution is None else f'{solution=}')
