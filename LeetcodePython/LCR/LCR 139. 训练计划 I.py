#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 10:17
FileName: LCR 139. 训练计划 I
Description:
"""
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        return sorted(actions, key=lambda action: action % 2, reverse=True)


if __name__ == '__main__':
    solution = Solution().trainingPlan(actions=[1, 2, 3, 4, 5])
    print(solution)
