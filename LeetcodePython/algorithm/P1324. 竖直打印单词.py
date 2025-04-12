#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 10:24
FileName: algorithm/P1324. 竖直打印单词.py
Description: 
"""
from typing import List
from itertools import zip_longest

from icecream import ic


class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(el).rstrip() for el in zip_longest(*[ch for ch in s.split()], fillvalue=' ')]


if __name__ == '__main__':
    solution = Solution().printVertically(s="TO BE OR NOT TO BE")
    ic(solution)
