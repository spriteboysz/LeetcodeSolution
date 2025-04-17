#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-17 23:59
FileName: LCR/P0677. 键值映射.py
Description: 
"""
from collections import defaultdict

from icecream import ic


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
    map_sum = MapSum()
    map_sum.insert('apple', 3)
    ic(map_sum.sum('ap'))
    map_sum.insert('app', 2)
