#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 22:02
FileName: P1678. 设计 Goal 解析器.py
Description:
"""


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == '__main__':
    solution = Solution().interpret(command = "G()()()()(al)")
    print(solution)
