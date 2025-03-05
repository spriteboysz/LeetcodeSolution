#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-05 22:11
FileName: algorithm/P1678. 设计 Goal 解析器.py
Description: 
"""

from icecream import ic


class Solution:
    def interpret(self, command: str) -> str:
        dic = {'()': 'o', '(al)': 'al'}
        for k, v in dic.items():
            command = command.replace(k, v)
        return command


if __name__ == '__main__':
    solution = Solution().interpret(command="G()()()()(al)")
    ic(solution)
