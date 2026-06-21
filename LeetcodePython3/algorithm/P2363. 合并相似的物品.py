#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 19:46
FileName: P2363. 合并相似的物品.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for value, weight in items1 + items2:
            dic[value] += weight
        return sorted([[v, w] for v, w in dic.items()])


if __name__ == '__main__':
    solution = Solution().mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])
    print(solution)
