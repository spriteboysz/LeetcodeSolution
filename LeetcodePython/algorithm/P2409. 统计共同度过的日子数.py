#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 22:49
FileName: P2409. 统计共同度过的日子数
Description:
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def process(date):
            mm, dd = map(int, date.split('-'))
            return sum(months[:mm]) + dd

        s1, e1 = process(arriveAlice), process(leaveAlice)
        s2, e2 = process(arriveBob), process(leaveBob)
        return max(min(e1, e2) - max(s1, s2) + 1, 0)


if __name__ == '__main__':
    solution = Solution().countDaysTogether("08-15", "08-18", "08-16", "08-19")
    print(solution)
