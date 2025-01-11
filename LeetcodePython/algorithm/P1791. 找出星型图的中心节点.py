#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 23:33
FileName: P1791. 找出星型图的中心节点
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


if __name__ == '__main__':
    solution = Solution().findCenter([[1, 2], [2, 3], [4, 2]])
    ic(solution)
