#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:46
FileName: LCR/P0705. 设计哈希集合.py
Description: 
"""

from icecream import ic


class MyHashSet:

    def __init__(self):
        self.seen = set()

    def add(self, key: int) -> None:
        self.seen.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.seen.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.seen


if __name__ == '__main__':
    seen = MyHashSet()
    seen.add(1)
    seen.add(2)
    seen.remove(1)
    ic(seen.contains(1))
