#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:26
FileName: algorithm/P3861. 容量最小的箱子.py
Description: 
"""


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minimum = min((cap for cap in capacity if cap >= itemSize), default=-1)
        for i, cap in enumerate(capacity):
            if cap == minimum:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().minimumIndex(capacity=[1, 5, 3, 7], itemSize=3)
    print('<None>' if solution is None else f'{solution=}')
