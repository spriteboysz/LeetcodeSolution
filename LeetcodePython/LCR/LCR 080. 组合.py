#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:43
FileName: LCR 080. 组合
Description:
"""
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(el) for el in itertools.combinations(range(1, n + 1), k)]


if __name__ == '__main__':
    solution = Solution().combine(4, 2)
    print(solution)
