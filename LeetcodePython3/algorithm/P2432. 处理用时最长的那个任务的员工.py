#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:17
FileName: P2432. 处理用时最长的那个任务的员工.py
Description:
"""
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs = [[0, 0], *logs]
        costs = [(logs[i][0], logs[i][1] - logs[i - 1][1]) for i in range(1, len(logs))]
        return max(costs, key=lambda cost: (cost[1], -cost[0]))[0]


if __name__ == '__main__':
    solution = Solution().hardestWorker(n=26, logs=[[1, 1], [3, 7], [2, 12], [7, 17]])
    print(solution)
