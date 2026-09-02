#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 14:44
FileName: LCR/LCR 083. 全排列.py
Description: 
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        visited = set()
        def backtrack(k, path):
            if k == len(nums):
                paths.append(path.copy())
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    backtrack(k + 1, path)
                    path.pop()
                    visited.remove(i)

        backtrack(0, [])
        return paths


if __name__ == '__main__':
    solution = Solution().permute([1, 2, 3])
    print(solution)
