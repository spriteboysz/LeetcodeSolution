#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:30
FileName: LC/LCR 178. 训练计划 VI.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        counter = Counter(actions)
        return [action for action, cnt in counter.items() if cnt == 1][0]


if __name__ == '__main__':
    solution = Solution().trainingPlan([12, 1, 6, 12, 6, 12, 6])
    print(solution)
