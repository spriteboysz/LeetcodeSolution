#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:19
FileName: P0771. 宝石与石头.py
Description:
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(jewel) for jewel in jewels)


if __name__ == '__main__':
    solution = Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
    print(solution)
