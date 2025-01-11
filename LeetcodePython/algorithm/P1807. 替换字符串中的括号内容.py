#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 22:14
FileName: P1807. 替换字符串中的括号内容
Description:
"""
import re
from typing import List

from icecream import ic


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = {k: v for k, v in knowledge}
        matches = re.findall(r'\(([a-z]+)\)', s)
        for match in matches:
            s = s.replace(f'({match})', dic.get(match, '?'))
        return s


if __name__ == '__main__':
    solution = Solution().evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]])
    ic(solution)
