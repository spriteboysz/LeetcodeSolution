#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 11:32
FileName: P1046. 最后一块石头的重量.py
Description:
"""
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            s1, s2 = stones.pop(), stones.pop()
            if s1 != s2:
                stones.append(abs(s1 - s2))
        return 0 if not stones else stones[-1]


if __name__ == '__main__':
    solution = Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
    print(solution)
