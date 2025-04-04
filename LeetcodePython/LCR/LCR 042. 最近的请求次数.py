#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 20:32
FileName: LCR/LCR 042. 最近的请求次数.py
Description: 
"""
from collections import deque

from icecream import ic


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == '__main__':
    recent_counter = RecentCounter()
    ic(recent_counter.ping(1))
    ic(recent_counter.ping(100))
    ic(recent_counter.ping(3001))
    ic(recent_counter.ping(3002))
