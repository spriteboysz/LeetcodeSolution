#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 13:46
FileName: algorithm/P3216. 交换后字典序最小的字符串.py
Description: 
"""


class Solution:
    def getSmallestString(self, s: str) -> str:
        ss = list(s)
        for i in range(1, len(ss)):
            a, b = int(ss[i - 1]), int(ss[i])
            if a % 2 != b % 2:
                continue
            if 10 * a + b > 10 * b + a:
                ss[i - 1], ss[i] = str(b), str(a)
                break
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().getSmallestString("45320")
    print('<None>' if solution is None else f'{solution=}')
