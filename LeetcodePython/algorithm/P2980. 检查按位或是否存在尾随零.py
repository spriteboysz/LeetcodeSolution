#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 22:07
FileName: P2980. 检查按位或是否存在尾随零
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(num % 2 == 0 for num in nums) >= 2


if __name__ == '__main__':
    solution = Solution().hasTrailingZeros([2, 3, 4, 5])
    ic(solution)
