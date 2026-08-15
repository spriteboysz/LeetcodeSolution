#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 10:17
FileName: algorithm/P0017. 电话号码的字母组合.py
Description: 
"""
from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboards = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combinations = []
        for item in product(*[keyboards.get(ch) for ch in digits]):
            combinations.append(''.join(item))
        return combinations


if __name__ == '__main__':
    solution = Solution().letterCombinations('23')
    print(solution)
