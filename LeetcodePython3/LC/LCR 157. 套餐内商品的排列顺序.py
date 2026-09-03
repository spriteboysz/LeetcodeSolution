#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:18
FileName: LC/LCR 157. 套餐内商品的排列顺序.py
Description: 
"""
from itertools import permutations

from typing import List


class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        seen = set()
        for perm in permutations(goods):
            seen.add(''.join(perm))
        return list(seen)


if __name__ == '__main__':
    solution = Solution().goodsOrder(goods="agew")
    print(solution)
