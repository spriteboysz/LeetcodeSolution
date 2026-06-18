#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-18 23:03
FileName: P0944. 删列造序.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(ch1 > ch2 for ch1, ch2 in pairwise(column)) for column in zip(*strs))


if __name__ == '__main__':
    solution = Solution().minDeletionSize(strs=["cba", "daf", "ghi"])
    print(solution)
