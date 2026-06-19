#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 20:50
FileName: P2469. 温度转换.py
Description:
"""
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]


if __name__ == '__main__':
    solution = Solution().convertTemperature(celsius=36.50)
    print(solution)
