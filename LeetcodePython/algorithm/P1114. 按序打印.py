#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-07 22:21
FileName: P1114. 按序打印.py
Description:
"""

import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.l2.acquire()
        printThird()


if __name__ == '__main__':
    s = Foo()
    print(s)
