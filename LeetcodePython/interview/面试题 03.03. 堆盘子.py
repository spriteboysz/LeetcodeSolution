#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 23:15
FileName: interview/面试题 03.03. 堆盘子.py
Description: 
"""

from icecream import ic


class StackOfPlates:

    def __init__(self, cap: int):
        self.stacks = []
        self.cap = cap

    def push(self, val: int) -> None:
        if not self.stacks or len(self.stacks[-1]) >= self.cap:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.popAt(-1)

    def popAt(self, index: int) -> int:
        if not self.stacks or len(self.stacks) <= index or self.cap == 0:
            return -1
        x = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return x


if __name__ == '__main__':
    stacks = StackOfPlates(1)
    stacks.push(1)
    stacks.push(2)
    ic(stacks.popAt(1))
    ic(stacks.pop())
    ic(stacks.pop())
