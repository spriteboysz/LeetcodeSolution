#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 21:52
FileName: LCR/P0706. 设计哈希映射.py
Description: 
"""

from icecream import ic


class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if key in self.dic:
            return self.dic[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic.pop(key)


if __name__ == '__main__':
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)
    ic(myHashMap.get(1))
    ic(myHashMap.get(3))
