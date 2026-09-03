#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:49
FileName: LC/LCR 158. 库存管理 II.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        counter = Counter(stock)
        for num, cnt in counter.items():
            if cnt > len(stock) / 2:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().inventoryManagement([6, 1, 3, 1, 1, 1])
    print(solution)
