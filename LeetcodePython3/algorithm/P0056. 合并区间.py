#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 22:26
FileName: P0056. 合并区间.py
Description:
"""
import doctest

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Example:
        >>> Solution().merge([[4, 7], [1, 4]])
        [[1, 7]]
        """

        intervals.sort()
        ranges = []
        for s, e in intervals:

            if not ranges or ranges[-1][-1] < s:
                ranges.append([s, e])
            else:
                ranges[-1][-1] = max(ranges[-1][-1], e)
        return ranges


if __name__ == '__main__':
    doctest.testmod(verbose=True)
