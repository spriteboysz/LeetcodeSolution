#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 16:32
FileName: interview/面试题 03.04. 化栈为队.py
Description: 
"""
from collections import deque

from icecream import ic


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        stack2 = deque()
        while self.stack:
            stack2.append(self.stack.pop())
        el = stack2.pop()
        while stack2:
            self.stack.append(stack2.pop())
        return el

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


if __name__ == '__main__':
    queue = MyQueue()
    ic(queue.push(1))
    ic(queue.push(2))
    ic(queue.peek())
    ic(queue.pop())
    ic(queue.empty())
