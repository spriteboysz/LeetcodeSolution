#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:13
FileName: P2798. 满足目标工作时长的员工数目.py
Description:
"""
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(num >= target for num in hours)


if __name__ == '__main__':
    solution = Solution().numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2)
    print(solution)
