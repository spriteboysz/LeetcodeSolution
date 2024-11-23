#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:57
FileName: P1491. 去掉最低工资和最高工资后的工资平均值
Description:
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


if __name__ == '__main__':
    solution = Solution().average(salary=[4000, 3000, 1000, 2000])
    print(solution)
