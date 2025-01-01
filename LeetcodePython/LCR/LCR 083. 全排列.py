#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 21:12
FileName: LCR 083. 全排列
Description:
"""
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(el) for el in permutations(nums)]


if __name__ == '__main__':
    solution = Solution().permute([1, 2, 3])
    print(solution)
