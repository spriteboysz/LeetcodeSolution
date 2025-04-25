#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-24 23:27
FileName: algorithm/P0039. 组合总和.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, path = [], []
        candidates.sort()
        n = len(candidates)

        def dfs(i, remain):
            if remain == 0:
                ans.append(path.copy())
                return
            for j in range(i, n):
                if candidates[j] <= remain:
                    path.append(candidates[j])
                    dfs(j, remain - candidates[j])
                    path.pop()
                else:
                    break

        dfs(0, target)
        return ans


if __name__ == '__main__':
    solution = Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
    ic(solution)
