#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 22:33
FileName: P0592. 分数加减运算
Description:
"""

from math import lcm, gcd

from icecream import ic


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-').lstrip('+')
        elements = [tuple(map(int, el.split('/'))) for el in expression.split('+')]
        denominator = lcm(*[el[1] for el in elements])
        numerator = sum(el[0] * denominator // el[1] for el in elements)
        common = gcd(numerator, denominator)
        return f'{numerator // common}/{denominator // common}'


if __name__ == '__main__':
    solution = Solution().fractionAddition(expression="-1/2+1/2+1/3")
    ic(solution)
