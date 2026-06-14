#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 18:57
FileName: P0682. 棒球比赛.py
Description:
"""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == '+':
                score.append(score[-1] + score[-2])
            elif op == 'D':
                score.append(score[-1] * 2)
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        return sum(score)


if __name__ == '__main__':
    solution = Solution().calPoints(["5","2","C","D","+"])
    print(solution)
