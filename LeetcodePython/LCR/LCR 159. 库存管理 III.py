#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:27
FileName: LCR 159. 库存管理 III
Description:
"""
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return sorted(stock)[:cnt]


if __name__ == '__main__':
    solution = Solution().inventoryManagement(stock=[2, 5, 7, 4], cnt=1)
    print(solution)
