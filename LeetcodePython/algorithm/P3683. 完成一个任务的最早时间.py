#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 16:33
FileName: P3683. 完成一个任务的最早时间.py
Description:
"""
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + e for s, e in tasks)


if __name__ == '__main__':
    s = Solution().earliestTime(tasks=[[1, 6], [2, 3]])
    print(s)
