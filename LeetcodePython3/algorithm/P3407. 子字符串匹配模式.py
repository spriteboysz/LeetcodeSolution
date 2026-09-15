#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 16:38
FileName: algorithm/P3407. 子字符串匹配模式.py
Description: 
"""
import re


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        return bool(re.findall(p.replace('*', '.*'), s))


if __name__ == '__main__':
    solution = Solution().hasMatch(s="leetcode", p="ee*e")
    print('<None>' if solution is None else f'{solution=}')
