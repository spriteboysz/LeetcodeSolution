#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-27 23:21
FileName: algorithm/P1016. 子串能表示从 1 到 N 数字的二进制串.py
Description: 
"""

from icecream import ic


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n):
            if bin(i + 1)[2:] not in s:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().queryString('0110', 3)
    ic(solution)
