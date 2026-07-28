#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:13
FileName: P0225. 用队列实现栈.py
Description:
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        return -1

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == '__main__':
    solution = MyStack()
    print(solution)
