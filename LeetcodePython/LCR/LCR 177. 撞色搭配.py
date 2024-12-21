#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 19:54
FileName: LCR 177. 撞色搭配
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        counter = Counter(sockets)
        return [k for k, v in counter.items() if v == 1]


if __name__ == '__main__':
    solution = Solution().sockCollocation(sockets=[4, 5, 2, 4, 6, 6])
    print(solution)
