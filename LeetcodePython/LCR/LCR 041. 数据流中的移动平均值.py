#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 23:14
FileName: LCR/LCR 041. 数据流中的移动平均值.py
Description: 
"""
from collections import deque

from icecream import ic


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)


if __name__ == '__main__':
    solution = MovingAverage(3)
    ic(solution.next(1))
    ic(solution.next(10))
    ic(solution.next(3))
    ic(solution.next(5))
