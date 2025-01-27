#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 21:41
FileName: P2660. 保龄球游戏的获胜者
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def process(player):
            score, k = 0, 0
            for num in player:
                if k > 0:
                    score += num * 2
                else:
                    score += num
                k -= 1
                if num == 10:
                    k = 2
            return score

        s1, s2 = process(player1), process(player2)
        if s1 == s2:
            return 0
        return 1 if s1 > s2 else 2


if __name__ == '__main__':
    solution = Solution().isWinner(player1=[5, 10, 3, 2], player2=[6, 5, 7, 3])
    ic(solution)
