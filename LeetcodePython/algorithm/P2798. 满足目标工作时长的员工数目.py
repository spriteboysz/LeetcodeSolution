#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 22:48
FileName: P2798. 满足目标工作时长的员工数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(hour >= target for hour in hours)


if __name__ == '__main__':
    solution = Solution().numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2)
    ic(solution)
