#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:16
FileName: P0232. 用栈实现队列.py
Description:
"""

from collections import deque


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.queue.popleft()
        return -1

    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
        return -1

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    solution = MyQueue()
    solution.push(1)
    solution.push(2)
    print(solution.peek())
    print(solution.pop())
    print(solution.empty())
