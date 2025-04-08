#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 22:50
FileName: LCR/LCR 157. 套餐内商品的排列顺序.py
Description: 
"""
from typing import List
from itertools import permutations

from icecream import ic


class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        return list({''.join(el) for el in permutations(goods)})


if __name__ == '__main__':
    solution = Solution().goodsOrder('abc')
    ic(solution)
