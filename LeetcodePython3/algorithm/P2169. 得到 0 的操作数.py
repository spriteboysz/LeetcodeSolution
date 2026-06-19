#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 12:27
FileName: P2169. 得到 0 的操作数.py
Description:
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 * num2 > 0:
            num1, num2 = sorted([num1, num2], reverse=True)
            num1 -= num2
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countOperations(2, 3)
    print(solution)
