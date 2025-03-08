#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:21
FileName: LCR/LCR 125. 图书整理 II.py
Description: 
"""

from icecream import ic


class CQueue:

    def __init__(self):
        self.queue = []

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        if not self.queue:
            return -1
        head = self.queue[0]
        self.queue = self.queue[1:]
        return head


if __name__ == '__main__':
    book_queue = CQueue()
    book_queue.appendTail(1)
    book_queue.appendTail(2)
    ic(book_queue.deleteHead())
