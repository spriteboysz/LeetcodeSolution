#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 19:32
FileName: P1450. 在既定时间做作业的学生人数.py
Description:
"""
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(a <= queryTime <= b for a, b in zip(startTime, endTime))


if __name__ == '__main__':
    solution = Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4)
    print(solution)
