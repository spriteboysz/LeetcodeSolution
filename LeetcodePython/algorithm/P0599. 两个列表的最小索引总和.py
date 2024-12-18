#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 23:53
FileName: P0599. 两个列表的最小索引总和
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = defaultdict(list)
        for i, el in enumerate(list1):
            dic[el].append(i)
        for i, el in enumerate(list2):
            dic[el].append(i)
        dic = {k: sum(v) for k, v in dic.items() if len(v) == 2}
        minimum = min(dic.values())
        return [k for k, v in dic.items() if v == minimum]


if __name__ == '__main__':
    solution = Solution().findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                         list2=["KFC", "Shogun", "Burger King"])
    print(solution)
