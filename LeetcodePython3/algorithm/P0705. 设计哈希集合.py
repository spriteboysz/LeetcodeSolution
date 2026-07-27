#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 21:30
FileName: P0705. 设计哈希集合.py
Description:
"""


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
    solution = MyHashSet()
    print(solution)
