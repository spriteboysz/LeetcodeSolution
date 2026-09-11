#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 14:49
FileName: algorithm/P2079. 给植物浇水.py
Description: 
"""
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        cnt = 0
        pos = 0
        while pos < len(plants):
            if curr >= plants[pos]:
                curr -= plants[pos]
                cnt += 1
                pos += 1
            else:
                cnt += pos * 2
                curr = capacity
        return cnt


if __name__ == '__main__':
    solution = Solution().wateringPlants(plants=[2, 2, 3, 3], capacity=5)
    print('<None>' if solution is None else f'{solution=}')
