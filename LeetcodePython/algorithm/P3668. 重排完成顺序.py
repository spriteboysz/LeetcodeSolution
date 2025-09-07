#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-07 22:24
FileName: P3668. 重排完成顺序.py
Description:
"""
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [el for el in order if el in friends]


if __name__ == '__main__':
    s = Solution().recoverOrder(order=[3, 1, 2, 5, 4], friends=[1, 3, 4])
    print(s)
