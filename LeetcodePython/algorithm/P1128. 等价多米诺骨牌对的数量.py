#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 23:13
FileName: P1128. 等价多米诺骨牌对的数量
Description:
"""
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        @lru_cache
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return factorial(num - 1) * num

        @lru_cache
        def combination(num, b=2):
            return factorial(num) // (factorial(b) * factorial(num - b))

        dominoes = [tuple(sorted(domino)) for domino in dominoes]
        return sum([combination(num) for num in Counter(dominoes).values() if num >= 2])


if __name__ == '__main__':
    solution = Solution().numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]])
    print(solution)
