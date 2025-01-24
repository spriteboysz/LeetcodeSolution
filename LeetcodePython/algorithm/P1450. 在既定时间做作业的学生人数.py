#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 21:43
FileName: P1450. 在既定时间做作业的学生人数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4)
    ic(solution)
