#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 08:47
FileName: algorithm/P1557. 可以到达所有点的最少点数目.py
Description: 
"""
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        lefts, rights = set(), set()
        for left, right in edges:
            lefts.add(left)
            rights.add(right)
        return list(lefts - rights)


if __name__ == '__main__':
    solution = Solution().findSmallestSetOfVertices(
        n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    )
    print(solution)
