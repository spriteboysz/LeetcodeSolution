#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 16:54
FileName: P0682. 棒球比赛
Description:
"""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i, operation in enumerate(operations):
            if operation == '+':
                points.append(points[-1] + points[-2])
            elif operation == 'D':
                points.append(points[-1] * 2)
            elif operation == 'C':
                points.pop()
            else:
                points.append(int(operation))
        return sum(points)


if __name__ == '__main__':
    solution = Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print(solution)
