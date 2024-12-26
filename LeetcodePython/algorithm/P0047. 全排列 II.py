#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:11
FileName: P0047. 全排列 II
Description:
"""
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permute = permutations(nums)
        return [list(el) for el in set(permute)]


if __name__ == '__main__':
    solution = Solution().permuteUnique([1, 1, 2])
    print(solution)
