#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-06 16:01
FileName: interview/P1557. 可以到达所有点的最少点数目.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        starts, ends = set(), set()
        for start, end in edges:
            starts.add(start)
            ends.add(end)
        return list(starts - ends) + list(set(range(0, n)) - starts - ends)


if __name__ == '__main__':
    solution = Solution().findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])
    ic(solution)
