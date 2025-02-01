#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 10:16
FileName: P1640. 能否连接形成数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for el in pieces:
            if el[0] not in arr:
                return False
        pieces.sort(key=lambda el: arr.index(el[0]))
        return arr == sum(pieces, [])


if __name__ == '__main__':
    solution = Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])
    ic(solution)
