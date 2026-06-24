#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 23:26
FileName: P1640. 能否连接形成数组.py
Description:
"""
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if set(arr) != set(sum(pieces, [])):
            return False
        pieces.sort(key=lambda el: arr.index(el[0]))
        return arr == sum(pieces, [])


if __name__ == '__main__':
    solution = Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])
    print(solution)
