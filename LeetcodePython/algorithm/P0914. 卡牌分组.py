#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 22:35
FileName: P0914. 卡牌分组
Description:
"""
import math
from collections import Counter
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        return math.gcd(*counter.values()) >= 2


if __name__ == '__main__':
    solution = Solution().hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1])
    print(solution)
