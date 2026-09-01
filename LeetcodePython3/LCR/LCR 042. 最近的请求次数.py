#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 11:22
FileName: LCR/LCR 042. 最近的请求次数.py
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
    recent_counter = RecentCounter()
    print(recent_counter.ping(1))
    print(recent_counter.ping(100))
    print(recent_counter.ping(3001))
    print(recent_counter.ping(3002))
