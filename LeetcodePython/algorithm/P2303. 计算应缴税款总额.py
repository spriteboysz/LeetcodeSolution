#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-23 18:00
FileName: P2303. 计算应缴税款总额
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax, curr = 0, 0
        for start, percent in brackets:
            if income > start:
                tax += percent / 100 * (start - curr)
            else:
                tax += percent / 100 * (income - curr)
                return tax
            curr = start

        return tax + (income - brackets[-1][0]) * brackets[-1][1] / 100


if __name__ == '__main__':
    solution = Solution().calculateTax(brackets=[[3, 50], [7, 10], [12, 25]], income=10)
    ic(solution)
