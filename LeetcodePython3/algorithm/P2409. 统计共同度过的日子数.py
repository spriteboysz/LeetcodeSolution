#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:05
FileName: P2409. 统计共同度过的日子数.py
Description:
"""


class Solution:
    @staticmethod
    def calc(date):
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mm, dd = map(int, date.strip().split('-'))
        return sum(months[:mm]) + dd

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive, leave = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        return max(0, self.calc(leave) - self.calc(arrive) + 1)


if __name__ == '__main__':
    solution = Solution().countDaysTogether(
        arriveAlice="10-01",
        leaveAlice="10-31",
        arriveBob="11-01",
        leaveBob="12-31"
    )
    print(solution)
