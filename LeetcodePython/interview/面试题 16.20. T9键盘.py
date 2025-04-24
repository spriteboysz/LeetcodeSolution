#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-24 23:13
FileName: interview/面试题 16.20. T9键盘.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
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
        return [word for word in words if all(ch in dic[digit] for ch, digit in zip(word, num))]


if __name__ == '__main__':
    solution = Solution().getValidT9Words(num="8733", words=["tree", "used", 'treg'])
    ic(solution)
