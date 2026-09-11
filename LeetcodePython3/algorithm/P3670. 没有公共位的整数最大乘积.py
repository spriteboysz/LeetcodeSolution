#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 14:09
FileName: algorithm/P3670. 没有公共位的整数最大乘积.py
Description: 
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = []
        nums = list(set(nums))
        for i, num1 in enumerate(nums):
            for num2 in nums[:i]:
                if num1 & num2 == 0:
                    products.append(num1 * num2)
        return max(products, default=0)


if __name__ == '__main__':
    solution = Solution().maxProduct([1, 2, 3, 4, 5, 6, 7])
    print('<None>' if solution is None else f'{solution=}')
