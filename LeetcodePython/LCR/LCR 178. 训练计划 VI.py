#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 19:57
FileName: LCR 178. 训练计划 VI
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        counter = Counter(actions)
        return [k for k, v in counter.items() if v == 1][0]


if __name__ == '__main__':
    solution = Solution().trainingPlan(actions=[12, 1, 6, 12, 6, 12, 6])
    print(solution)
