#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 23:01
FileName: P3238. 求出胜利玩家的数目
Description:
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i, color in pick:
            dic[i].append(color)
        counter = {i: max(Counter(v).values()) for i, v in dic.items()}
        return sum([v > k for k, v in counter.items()])


if __name__ == '__main__':
    solution = Solution().winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])
    print(solution)
