#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-22 23:29
FileName: algorithm/P0017. 电话号码的字母组合.py
Description: 
"""
from typing import List
from itertools import product

from icecream import ic


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return [''.join(el) for el in product(*[dic[ch] for ch in digits])]


if __name__ == '__main__':
    solution = Solution().letterCombinations('23')
    ic(solution)
