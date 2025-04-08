#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 23:21
FileName: interview/面试题 03.02. 栈的最小值.py
Description: 
"""

from icecream import ic


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self) -> None:
        x = self.stack1.pop()
        if x == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        return -1

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]
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
