#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 22:32
FileName: P0046. 全排列
Description:
"""
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(el) for el in permutations(nums)]


if __name__ == '__main__':
    solution = Solution().permute([1, 2, 3])
    print(solution)
