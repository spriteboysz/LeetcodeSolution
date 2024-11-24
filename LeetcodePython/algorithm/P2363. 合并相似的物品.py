#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 09:14
FileName: P2363. 合并相似的物品
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for v, w in [*items1, *items2]:
            dic[v] += w
        return sorted([[k, v] for k, v in dic.items()])


if __name__ == '__main__':
    solution = Solution().mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])
    print(solution)
