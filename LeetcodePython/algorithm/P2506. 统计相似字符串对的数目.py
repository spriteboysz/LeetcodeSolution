#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 23:21
FileName: P2506. 统计相似字符串对的数目
Description:
"""

from collections import Counter
from math import comb
from typing import List

from icecream import ic


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words2 = [tuple(sorted(set(word))) for word in words]
        counter = Counter(words2)
        return sum(comb(cnt, 2) for cnt in counter.values() if cnt >= 2)


if __name__ == '__main__':
    solution = Solution().similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"])
    ic(solution)
