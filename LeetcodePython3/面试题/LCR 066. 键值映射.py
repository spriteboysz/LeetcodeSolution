#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:20
FileName: 面试题/LCR 066. 键值映射.py
Description: 
"""
from collections import defaultdict


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.dic.items() if k.startswith(prefix))


if __name__ == '__main__':
    solution = MapSum()
    solution.insert('apple', 3)
    print(solution.sum('ap'))
    solution.insert('app', 2)
    print(solution.sum('ap'))
