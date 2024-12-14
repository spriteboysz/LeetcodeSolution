#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 11:47
FileName: LCR 158. 库存管理 II
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        dic = defaultdict(int)
        for num in stock:
            dic[num] += 1
        return [k for k, v in dic.items() if v > len(stock) // 2][0]


if __name__ == '__main__':
    solution = Solution().inventoryManagement(stock=[6, 1, 3, 1, 1, 1])
    print(solution)
