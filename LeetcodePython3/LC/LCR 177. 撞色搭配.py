#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 08:57
FileName: LC/LCR 177. 撞色搭配.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        counter = Counter(sockets)
        return [sock for sock, cnt in counter.items() if cnt == 1]


if __name__ == '__main__':
    solution = Solution().sockCollocation([4, 5, 2, 4, 6, 6])
    print(solution)
