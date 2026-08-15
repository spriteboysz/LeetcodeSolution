#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 21:10
FileName: algorithm/P2225. 找出输掉零场或一场比赛的玩家.py
Description: 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = set(), defaultdict(int)
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        return [sorted(set(winners) - set(losers)),
                sorted(i for i, v in losers.items() if v == 1)]


if __name__ == '__main__':
    solution = Solution().findWinners(
        [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    )
    print(solution)
