#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:55
FileName: P0997. 找到小镇的法官.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []:
            return 1

        dic = defaultdict(set)
        seen = set()
        for src, dst in trust:
            seen.add(src)
            dic[dst].add(src)
        # print(dic)
        for k, v in dic.items():
            if k not in seen and {k} | v == set(range(1, n + 1)) and k not in v:
                return k
        return -1


if __name__ == '__main__':
    solution = Solution().findJudge(n=1, trust=[])
    print(solution)
