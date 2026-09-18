#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 16:54
FileName: algorithm/P1324. 竖直打印单词.py
Description: 
"""
from itertools import zip_longest

from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        ss = []
        for el in zip_longest(*words, fillvalue=' '):
            ss.append(''.join(el).rstrip())
        return ss


if __name__ == '__main__':
    solution = Solution().printVertically("TO BE OR NOT TO BE")
    print('<None>' if solution is None else f'{solution=}')
