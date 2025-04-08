#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 23:27
FileName: LCR/LCR 147. 最小栈.py
Description: 
"""

from icecream import ic


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minimum or x <= self.minimum[-1]:
            self.minimum.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1]
        return -1


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    ic(min_stack.getMin())
    min_stack.pop()
    ic(min_stack.top())
    ic(min_stack.getMin())
