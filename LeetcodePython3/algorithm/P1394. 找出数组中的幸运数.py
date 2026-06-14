#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:42
FileName: P1394. 找出数组中的幸运数.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([k for k, v in Counter(arr).items() if k == v], default=-1)


if __name__ == '__main__':
    solution = Solution().findLucky(arr=[2, 2, 3, 4])
    print(solution)
