#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:49
FileName: P0599. 两个列表的最小索引总和.py
Description:
"""
from collections import defaultdict

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = defaultdict(list)
        for i, word in enumerate(list1):
            dic[word].append(i)
        for i, word in enumerate(list2):
            dic[word].append(i)
        common = {word: sum(v) for word, v in dic.items() if len(v) == 2}
        minimum = min(common.values())
        return [word for word, cnt in common.items() if cnt == minimum]


if __name__ == '__main__':
    solution = Solution().findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    )
    print(solution)
