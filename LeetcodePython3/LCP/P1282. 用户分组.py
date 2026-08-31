#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 23:10
FileName: LCP/P1282. 用户分组.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        for i, size in enumerate(groupSizes):
            dic[size].append(i)

        groups = []
        for i, v in dic.items():
            for j in range(0, len(v), i):
                groups.append(v[j:j + i])
        return groups


if __name__ == '__main__':
    solution = Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2])
    print(solution)
