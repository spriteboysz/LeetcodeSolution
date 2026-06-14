#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 18:59
FileName: P1491. 去掉最低工资和最高工资后的工资平均值.py
Description:
"""
from typing import List
from statistics import mean


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return mean(salary[1:-1])


if __name__ == '__main__':
    solution = Solution().average(salary=[4000, 3001, 1000, 2000])
    print(solution)
