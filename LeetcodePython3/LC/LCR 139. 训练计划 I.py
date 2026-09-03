#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:52
FileName: LC/LCR 139. 训练计划 I.py
Description: 
"""
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        odd = [action for action in actions if action % 2 == 1]
        even = [action for action in actions if action % 2 == 0]
        return odd + even


if __name__ == '__main__':
    solution = Solution().trainingPlan([1, 2, 3, 4, 5])
    print(solution)
