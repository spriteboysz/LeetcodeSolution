#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-30 15:57
FileName: interview/面试题 08.08. 有重复字符串的排列组合.py
Description: 
"""
from typing import List
from itertools import permutations

from icecream import ic


class Solution:
    def permutation(self, S: str) -> List[str]:
        return list({''.join(el) for el in permutations(S)})


if __name__ == '__main__':
    solution = Solution().permutation('eqq')
    ic(solution)
