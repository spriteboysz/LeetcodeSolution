#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 11:58
FileName: P2960. 统计已测试设备
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] <= 0:
                continue
            cnt += 1
            for j in range(i + 1, len(batteryPercentages)):
                batteryPercentages[j] -= 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countTestedDevices(batteryPercentages=[2, 1])
    ic(solution)
