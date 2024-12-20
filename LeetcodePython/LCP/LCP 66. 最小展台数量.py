#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 22:03
FileName: LCP 66. 最小展台数量
Description:
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        dic = defaultdict(int)
        for day in demand:
            counter = Counter(day)
            for k, v in counter.items():
                dic[k] = max(dic[k], v)
        return sum(dic.values())


if __name__ == '__main__':
    solution = Solution().minNumBooths(demand=["acd", "bed", "accd"])
    print(solution)
