#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 20:25
FileName: algorithm/P0040. 组合总和 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue
                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    solution = Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    ic(solution)
