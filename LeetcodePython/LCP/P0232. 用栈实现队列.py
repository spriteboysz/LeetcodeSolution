#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 16:42
FileName: LCP/P0232. 用栈实现队列.py
Description: 
"""
from collections import deque

from icecream import ic


class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        num = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return num

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1


if __name__ == '__main__':
    queue = MyQueue()
    ic(queue.push(1))
    ic(queue.push(2))
    ic(queue.peek())
    ic(queue.pop())
    ic(queue.empty())
