#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 16:38
FileName: P0640. 求解方程.py
Description:
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_items = left.replace('-', '+-').lstrip('+').split('+')
        right_items = right.replace('-', '+-').lstrip('+').split('+')
        left_c, right_c = 0, 0
        for item in left_items:
            if item.endswith('x'):
                if item == 'x' or item == '-x':
                    item = item.replace('x', '1')
                else:
                    item = item[:-1]
                left_c += int(item)
            else:
                right_c += -int(item)
        for item in right_items:
            if item.endswith('x'):
                if item == 'x' or item == '-x':
                    item = item.replace('x', '1')
                else:
                    item = item[:-1]
                left_c += -int(item)
            else:
                right_c += int(item)
        if left_c == 0 and right_c == 0:
            return 'Infinite solutions'
        if left_c == 0:
            return 'No solution'
        return f'x={right_c // left_c}'


if __name__ == '__main__':
    solution = Solution().solveEquation(equation="-x=-1")
    print(solution)
