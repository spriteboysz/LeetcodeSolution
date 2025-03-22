#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-22 21:32
FileName: algorithm/P3216. 交换后字典序最小的字符串.py
Description: 
"""

from icecream import ic


class Solution:
    def getSmallestString(self, s: str) -> str:
        ss = list(s)
        for i in range(1, len(ss)):
            a, b = int(ss[i - 1]), int(ss[i])
            if a % 2 == b % 2 and a > b:
                ss[i - 1], ss[i] = ss[i], ss[i - 1]
                break
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().getSmallestString(s="45320")
    ic(solution)
