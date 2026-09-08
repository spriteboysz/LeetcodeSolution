#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:17
FileName: 面试题/面试题 16.20. T9键盘.py
Description: 
"""
from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        keyboards = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        dic = {c: k for k, v in keyboards.items() for c in v}
        return [word for word in words if ''.join(dic.get(c, '0') for c in word) == num]


if __name__ == '__main__':
    solution = Solution().getValidT9Words(num="8733", words=["tree", "used"])
    print('<None>' if not solution else f'{solution=}')
