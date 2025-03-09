#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 21:55
FileName: interview/面试题 08.07. 无重复字符串的排列组合.py
Description: 
"""
from typing import List
from itertools import permutations

from icecream import ic


class Solution:
    def permutation(self, s: str) -> List[str]:
        return [''.join(el) for el in permutations(list(s))]


if __name__ == '__main__':
    solution = Solution().permutation('abc')
    ic(solution)
