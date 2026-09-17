#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 13:41
FileName: algorithm/P3238. 求出胜利玩家的数目.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic = defaultdict(lambda: defaultdict(int))
        for num, color in pick:
            dic[num][color] += 1
        return sum(max(v.values()) > num for num, v in dic.items())


if __name__ == '__main__':
    solution = Solution().winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])
    print('<None>' if solution is None else f'{solution=}')
