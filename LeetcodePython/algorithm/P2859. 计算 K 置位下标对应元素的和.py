#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-06 23:18
FileName: P2859. 计算 K 置位下标对应元素的和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums) if i.bit_count() == k)


if __name__ == '__main__':
    solution = Solution().sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1)
    ic(solution)
