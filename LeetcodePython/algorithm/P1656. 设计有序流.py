#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 20:37
FileName: algorithm/P1656. 设计有序流.py
Description: 
"""
from typing import List

from icecream import ic


class OrderedStream:

    def __init__(self, n: int):
        self.ss = [''] * n
        self.position = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ss[idKey - 1] = value
        stream = []
        while self.position < len(self.ss) and self.ss[self.position]:
            stream.append(self.ss[self.position])
            self.position += 1
        return stream


if __name__ == '__main__':
    ordered_stream = OrderedStream(5)
    ic(ordered_stream.insert(3, 'ccccc'))
    ic(ordered_stream.insert(1, 'aaaaa'))
    ic(ordered_stream.insert(2, 'bbbbb'))
    ic(ordered_stream.insert(5, 'eeeee'))
    ic(ordered_stream.insert(4, 'ddddd'))
