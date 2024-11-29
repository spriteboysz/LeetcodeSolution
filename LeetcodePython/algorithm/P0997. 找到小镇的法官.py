#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 22:56
FileName: P0997. 找到小镇的法官
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingress, egress = set(), defaultdict(set)
        for a, b in trust:
            ingress.add(a)
            egress[b].add(a)
        for num in range(1, n + 1):
            if len(egress[num]) == n - 1 and num not in ingress:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().findJudge(n=3, trust=[[1, 3], [2, 3]])
    print(solution)
