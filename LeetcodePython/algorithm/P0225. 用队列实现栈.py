#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:00
FileName: LCR/P0225. 用队列实现栈.py
Description: 
"""


class MyStack:

    def __init__(self):
        self.stack = []

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
        return not self.stack


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
