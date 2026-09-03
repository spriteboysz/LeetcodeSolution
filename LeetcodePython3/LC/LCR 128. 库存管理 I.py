#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 19:39
FileName: LC/LCR 128. 库存管理 I.py
Description: 
"""
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        return min(stock)


if __name__ == '__main__':
    solution = Solution().inventoryManagement(stock=[4, 5, 8, 3, 4])
    print(solution)
