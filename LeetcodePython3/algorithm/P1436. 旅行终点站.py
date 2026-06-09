#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 22:51
FileName: P1436. 旅行终点站.py
Description:
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dst = [path[0] for path in paths], [path[1] for path in paths]
        for city in dst:
            if city not in src:
                return city
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
    print(solution)
