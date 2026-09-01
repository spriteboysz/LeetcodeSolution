#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 11:07
FileName: 面试题/面试题 08.04. 幂集.py
Description: 
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        paths, path = [], []

        def backtrack(i: int) -> None:
            paths.append(path.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return paths


if __name__ == '__main__':
    solution = Solution().subsets([1, 2, 3])
    print(solution)
