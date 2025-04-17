#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-17 23:26
FileName: algorithm/P0478. 在圆内随机生成点.py
Description: 
"""
import random
import math
from typing import List

from icecream import ic


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.area = math.pi * radius ** 2

    def randPoint(self) -> List[float]:
        theta = random.uniform(0.0, math.pi * 2)
        r = math.sqrt(random.uniform(0.0, self.area) / math.pi)
        return [self.x + math.cos(theta) * r, self.y + math.sin(theta) * r]


if __name__ == '__main__':
    solution = Solution(1.0, 0.0, 0.0)
    ic(solution.randPoint())
    ic(solution.randPoint())
    ic(solution.randPoint())
