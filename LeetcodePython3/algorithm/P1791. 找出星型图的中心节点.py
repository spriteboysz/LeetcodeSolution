#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:05
FileName: P1791. 找出星型图的中心节点.py
Description:
"""
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]) & set(edges[1]))[0]


if __name__ == '__main__':
    solution = Solution().findCenter(edges=[[1, 2], [2, 3], [4, 2]])
    print(solution)
