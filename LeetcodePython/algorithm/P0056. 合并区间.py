#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 21:41
FileName: P0056. 合并区间
Description:
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ranges = []
        left,right = intervals[0]
        for s, e in intervals[1:]:
            if s > right:
                ranges.append([left, right])
                left = s
            right = max(right, e)
        ranges.append([left, right])
        return ranges



if __name__ == '__main__':
    solution = Solution().merge([[1, 4], [0, 0]])
    print(solution)
