#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 22:43
FileName: interview/面试题 03.01. 三合一.py
Description: 
"""

from icecream import ic


class TripleInOne:

    def __init__(self, stackSize: int):
        self.stacks = [[] for _ in range(3)]
        self.size = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stacks[stackNum]) >= self.size:
            return
        self.stacks[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stacks[stackNum].pop()

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stacks[stackNum][-1]

    def isEmpty(self, stackNum: int) -> bool:
        return not self.stacks[stackNum]


if __name__ == '__main__':
    stack = TripleInOne(2)
    stack.push(0, 1)
    stack.push(0, 2)
    stack.push(0, 3)
    ic(stack.pop(0))
    ic(stack.pop(0))
    ic(stack.pop(0))
    ic(stack.peek(0))
