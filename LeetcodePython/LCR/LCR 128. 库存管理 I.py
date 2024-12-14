#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:36
FileName: LCR 128. 库存管理 I
Description:
"""
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        return min(stock)


if __name__ == '__main__':
    solution = Solution().inventoryManagement(stock=[4, 5, 8, 3, 4])
    print(solution)
