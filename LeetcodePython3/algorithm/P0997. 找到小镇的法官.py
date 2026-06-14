#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:55
FileName: P0997. 找到小镇的法官.py
Description:
"""
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        src, dst = set(), set()
        for a, b in trust:
            src.add(a)
            dst.add(b)
        if len(dst) == 1 and src & dst == set() and src | dst == set(range(1, n + 1)):
            return trust[-1][-1]
        return -1


if __name__ == '__main__':
    solution = Solution().findJudge(n=3, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    print(solution)
