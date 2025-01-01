#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:40
FileName: LCR 079. 子集
Description:
"""
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums) + 1):
            subsets.extend(map(lambda el: list(el), combinations(nums, i)))
        return subsets


if __name__ == '__main__':
    solution = Solution().subsets([1,2,3])
    print(solution)