#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 21:01
FileName: algorithm/P1743. 从相邻元素对还原数组.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for a, b in adjacentPairs:
            dic[a].append(b)
            dic[b].append(a)
        nums = []
        for k, v in dic.items():
            if len(v) == 1:
                nums.append(k)
                nums.append(v[0])
                break
        while len(dic[nums[-1]]) == 2:
            for num in dic[nums[-1]]:
                if num == nums[-2]:
                    continue
                nums.append(num)
                break
        return nums



if __name__ == '__main__':
    solution = Solution().restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]])
    ic(solution)
