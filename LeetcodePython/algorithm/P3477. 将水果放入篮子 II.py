#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 22:25
FileName: algorithm/P3477. 将水果放入篮子 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        for fruit in fruits:
            for j, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[j] = -1
                    break
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numOfUnplacedFruits(fruits=[4, 2, 5], baskets=[3, 5, 4])
    ic(solution)
