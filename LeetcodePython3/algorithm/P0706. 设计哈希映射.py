#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 21:33
FileName: P0706. 设计哈希映射.py
Description:
"""


class MyHashMap:

    def __init__(self):
        self.dic = dict()

    def put(self, key: int, value: int) -> None:
        self.dic.update({key: value})

    def get(self, key: int) -> int:
        return self.dic.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic.pop(key)


if __name__ == '__main__':
    solution = MyHashMap()
    print(solution)
