#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 10:24
FileName: P2660. 保龄球游戏的获胜者.py
Description:
"""
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc(player):
            for i in range(len(player) - 1, 0, -1):
                if player[i - 1] == 10 or (i >= 2 and player[i - 2] == 10):
                    player[i] *= 2
            return sum(player)

        sum1, sum2 = calc(player1), calc(player2)
        if sum1 == sum2:
            return 0
        return 1 if sum1 > sum2 else 2


if __name__ == '__main__':
    solution = Solution().isWinner(player1=[5, 10, 3, 2], player2=[6, 5, 7, 3])
    print(solution)
