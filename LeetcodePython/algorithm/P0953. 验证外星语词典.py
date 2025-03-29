#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-29 22:46
FileName: algorithm/P0953. 验证外星语词典.py
Description: 
"""

from typing import List
from string import ascii_lowercase as lowercase

from icecream import ic


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = str.maketrans(order, lowercase)
        words = [word.translate(table) for word in words]
        return words == sorted(words)


if __name__ == '__main__':
    solution = Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    ic(solution)
