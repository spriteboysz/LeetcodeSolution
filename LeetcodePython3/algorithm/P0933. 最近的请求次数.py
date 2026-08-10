#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 22:52
FileName: P0933. 最近的请求次数.py
Description:
"""
from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and t - self.queue[0] > 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)


if __name__ == '__main__':
    solution = RecentCounter()
    print(solution.ping(1))
    print(solution.ping(100))
    print(solution.ping(3001))
    print(solution.ping(3002))
