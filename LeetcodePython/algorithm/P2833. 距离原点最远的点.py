#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 11:51
FileName: P2833. 距离原点最远的点
Description:
"""

from icecream import ic


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt1, cnt2 = 0, 0
        for move in moves:
            if move == 'L':
                cnt1 += 1
            elif move == 'R':
                cnt1 -= 1
            else:
                cnt2 += 1
        return abs(cnt1) + cnt2


if __name__ == '__main__':
    solution = Solution().furthestDistanceFromOrigin(moves="L_RL__R")
    ic(solution)
