#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 00:34
FileName: algorithm/P0039. 组合总和.py
Description: 
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []

        def backtrack(t, path, k):
            if t == 0:
                paths.append(path[:])
                return
            if t < 0:
                return
            for i in range(k, len(candidates)):
                path.append(candidates[i])
                backtrack(t - candidates[i], path, i)
                path.pop()

        backtrack(target, [], 0)
        return paths


if __name__ == '__main__':
    solution = Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(solution)
