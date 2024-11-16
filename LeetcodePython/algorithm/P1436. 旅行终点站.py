#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 14:15
FileName: P1436. 旅行终点站
Description:
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for s, e in paths:
            start.add(s)
            end.add(e)
        return list(end - start)[0]


if __name__ == '__main__':
    solution = Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
    print(solution)
