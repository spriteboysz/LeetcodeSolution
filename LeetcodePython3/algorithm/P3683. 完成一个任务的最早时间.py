#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 22:47
FileName: P3683. 完成一个任务的最早时间.py
Description:
"""
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(start + d for start, d in tasks)


if __name__ == '__main__':
    solution = Solution().earliestTime(tasks=[[1, 6], [2, 3]])
    print(solution)
