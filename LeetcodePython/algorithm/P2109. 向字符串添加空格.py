#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-25 09:54
FileName: algorithm/P2109. 向字符串添加空格.py
Description: 
"""
from typing import List
from itertools import pairwise

from icecream import ic


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(len(s))  # 这样可以在循环中处理最后一段
        ss = [s[:spaces[0]]]
        for p, q in pairwise(spaces):
            ss.append(' ')
            ss.append(s[p: q])
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15])
    ic(solution)
