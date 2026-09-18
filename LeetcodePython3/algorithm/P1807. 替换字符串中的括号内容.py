#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 16:08
FileName: algorithm/P1807. 替换字符串中的括号内容.py
Description: 
"""
import re
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = dict()
        for k, v in knowledge:
            dic[k] = v
        matches = re.findall(r'\(([a-z]+)\)', s)
        if not matches:
            return s
        keys = set(matches)
        for key in keys:
            s = s.replace(f'({key})', dic.get(key, '?'))
        return s


if __name__ == '__main__':
    solution = Solution().evaluate(
        s="(name)is(age)yearsold",
        knowledge=[["name", "bob"], ["age", "two"]]
    )
    print('<None>' if solution is None else f'{solution=}')
