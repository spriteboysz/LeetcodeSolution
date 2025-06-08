#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-08 10:11
FileName: algorithm/P2924. 找到冠军 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        seen = set(range(n)) - {edge[1] for edge in edges}
        if len(seen) == 1:
            return seen.pop()
        return -1


if __name__ == '__main__':
    solution = Solution().findChampion(n=3, edges=[[0, 1], [1, 2]])
    ic(solution)
