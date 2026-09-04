#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:53
FileName: 面试题/面试题 16.26. 计算器.py
Description: 
"""


class Solution:
    def calculate(self, s: str) -> int:
        return eval(s.replace('/', '//'))


if __name__ == '__main__':
    solution = Solution().calculate('3+2*2')
    print(solution)
