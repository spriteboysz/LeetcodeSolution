#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-18 22:49
FileName: P1860. 增长的内存泄露
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cnt = 1
        while memory1 >= cnt or memory2 >= cnt:
            if memory1 >= memory2:
                memory1 -= cnt
            else:
                memory2 -= cnt
            cnt += 1
        return [cnt, memory1, memory2]


if __name__ == '__main__':
    solution = Solution().memLeak(memory1=2, memory2=2)
    ic(solution)
