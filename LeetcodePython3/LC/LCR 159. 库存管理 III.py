#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 16:33
FileName: LC/LCR 159. 库存管理 III.py
Description: 
"""
import heapq

from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        heapq.heapify(stock)
        return heapq.nsmallest(cnt, stock)


if __name__ == '__main__':
    solution = Solution().inventoryManagement(stock=[0, 2, 3, 6], cnt=2)
    print(solution)
