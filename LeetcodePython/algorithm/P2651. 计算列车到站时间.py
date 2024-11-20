#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 23:35
FileName: P2651. 计算列车到站时间
Description:
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == '__main__':
    solution = Solution().findDelayedArrivalTime(13, 11)
    print(solution)
