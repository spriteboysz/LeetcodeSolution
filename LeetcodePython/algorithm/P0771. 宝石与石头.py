#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:09
FileName: P0771. 宝石与石头
Description:
"""

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        return sum([counter.get(jewel, 0) for jewel in jewels])


if __name__ == '__main__':
    solution = Solution().numJewelsInStones(jewels="aA", stones="aAAbbbb")
    print(solution)
