#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:41
FileName: LC/LCR 179. 查找总价格为目标值的两个商品.py
Description: 
"""
from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left, right = 0, len(price) - 1
        while left < right:
            if price[left] + price[right] == target:
                return [price[left], price[right]]
            if price[left] + price[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().twoSum(price=[3, 9, 12, 15], target=18)
    print(solution)
