#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-27 22:15
FileName: P0090. 子集 II
Description:
"""

from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = {tuple(sorted(el)) for count in range(len(nums) + 1) for el in combinations(nums, count)}
        return [list(el) for el in subsets]


if __name__ == '__main__':
    solution = Solution().subsetsWithDup([1, 2, 2])
    print(solution)
