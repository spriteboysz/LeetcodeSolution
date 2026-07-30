#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 21:07
FileName: P2960. 统计已测试设备.py
Description:
"""
from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt, n = 0, len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] > 0:
                cnt += 1
                for j in range(i + 1, n):
                    batteryPercentages[j] -= 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3])
    print(solution)
