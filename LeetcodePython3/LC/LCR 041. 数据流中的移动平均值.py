#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:11
FileName: LC/LCR 041. 数据流中的移动平均值.py
Description: 
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            v = self.queue.popleft()
            self.total -= v
        return self.total / len(self.queue)


if __name__ == '__main__':
    solution = MovingAverage(3)
    print(solution.next(1))
    print(solution.next(10))
    print(solution.next(3))
    print(solution.next(5))
