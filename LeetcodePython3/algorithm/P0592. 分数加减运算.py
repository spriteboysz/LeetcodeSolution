#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:43
FileName: P0592. 分数加减运算.py
Description:
"""
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-').lstrip('+')
        items = [[int(digit) for digit in item.split('/')] for item in expression.split('+')]
        denominator = math.lcm(*[item[1] for item in items])
        numerator = sum(item[0] * denominator // item[1] for item in items)
        gcd = math.gcd(denominator, numerator)
        return f'{numerator // gcd}/{denominator // gcd}'


if __name__ == '__main__':
    solution = Solution().fractionAddition(expression="-1/200+1/2+1/3")
    print(solution)
