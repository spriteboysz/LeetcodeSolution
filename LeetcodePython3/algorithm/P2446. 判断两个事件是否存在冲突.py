#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:14
FileName: P2446. 判断两个事件是否存在冲突.py
Description:
"""
from typing import List


class Solution:
    @staticmethod
    def calc(time):
        hh, mm = map(int, time.strip().split(':'))
        return hh * 60 + mm

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start, end = max(event1[0], event2[0]), min(event1[1], event2[1])
        return self.calc(end) - self.calc(start) >= 0


if __name__ == '__main__':
    solution = Solution().haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"])
    print(solution)
