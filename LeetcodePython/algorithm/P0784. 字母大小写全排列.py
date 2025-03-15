#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 20:20
FileName: algorithm/P0784. 字母大小写全排列.py
Description: 
"""
from typing import List

from icecream import ic
from itertools import product


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        indexes = [i for i, ch in enumerate(s) if ch.isalpha()]
        curr, ss = [ch for ch in s], []
        for el in product(*[(ch.lower(), ch.upper()) for ch in s if ch.isalpha()]):
            for index, ch in zip(indexes, el):
                curr[index] = ch
            ss.append(''.join(curr))
        return ss


if __name__ == '__main__':
    solution = Solution().letterCasePermutation('a1b2')
    ic(solution)
