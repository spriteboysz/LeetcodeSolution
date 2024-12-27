#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:51
FileName: P0078. 子集
Description:
"""
from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(el) for count in range(len(nums) + 1) for el in combinations(nums, count)]


if __name__ == '__main__':
    solution = Solution().subsets([1, 2, 3])
    print(solution)
