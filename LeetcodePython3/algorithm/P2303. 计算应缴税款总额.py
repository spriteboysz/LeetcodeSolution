#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 09:51
FileName: P2303. 计算应缴税款总额.py
Description:
"""
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax, curr = 0, 0
        for base, percent in brackets:
            if income >= base:
                tax += (base - curr) * percent
                curr = base
            else:
                tax += (income - curr) * percent
                break
        return tax / 100


if __name__ == '__main__':
    solution = Solution().calculateTax(brackets=[[3, 50], [7, 10], [12, 25]], income=10)
    print(solution)
