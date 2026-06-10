#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:26
FileName: P2833. 距离原点最远的点.py
Description:
"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt1, cnt2, cnt3 = moves.count('L'), moves.count('R'), moves.count('_')
        return max(cnt1, cnt2) - min(cnt1, cnt2) + cnt3


if __name__ == '__main__':
    solution = Solution().furthestDistanceFromOrigin(moves="_R__LL_")
    print(solution)
