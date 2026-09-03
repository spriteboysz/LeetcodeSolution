#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:23
FileName: LC/LCR 125. 图书整理 II.py
Description: 
"""
from collections import deque


class CQueue:

    def __init__(self):
        self.queue = deque()

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        if not self.queue:
            return -1
        return self.queue.popleft()


if __name__ == '__main__':
    solution = CQueue()
    solution.appendTail(1)
    solution.appendTail(2)
    print(solution.deleteHead())
