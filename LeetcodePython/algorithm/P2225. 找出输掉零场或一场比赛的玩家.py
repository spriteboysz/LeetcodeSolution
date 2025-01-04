#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:48
FileName: P2225. 找出输掉零场或一场比赛的玩家
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen1, dic2 = set(), defaultdict(int)
        for winner, loser in matches:
            seen1.add(winner)
            dic2[loser] += 1
        return [sorted(seen1 - set(dic2)), sorted(num for num, cnt in dic2.items() if cnt == 1)]


if __name__ == '__main__':
    solution = Solution().findWinners(
        [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]])
    ic(solution)
