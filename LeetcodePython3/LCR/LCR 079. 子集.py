#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 08:25
FileName: LCR/LCR 079. 子集.py
Description: 
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i: int) -> None:
            paths.append(path.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        paths, path = [], []
        backtrack(0)
        return paths


if __name__ == '__main__':
    solution = Solution().subsets([1, 2, 3])
    print(solution)
