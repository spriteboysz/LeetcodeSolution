#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 12:54
FileName: algorithm/P1268. 搜索推荐系统.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        dic = defaultdict(list)
        for product in products:
            for i in range(len(product)):
                dic[product[:i + 1]].append(product)

        for k, v in dic.items():
            v.sort()
            # print(k, v)
        return [dic[searchWord[:i + 1]][:3] for i in range(len(searchWord))]


if __name__ == '__main__':
    solution = Solution().suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse")
    ic(solution)
