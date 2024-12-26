#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:46
FileName: P0077. 组合
Description:
"""
from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(el) for el in combinations(range(1, n + 1), k)]

if __name__ == '__main__':
    solution = Solution().combine(4, 2)
    print(solution)