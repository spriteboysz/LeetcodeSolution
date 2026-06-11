#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:45
FileName: P2418. 按身高排序.py
Description:
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = [(name, height) for name, height in zip(names, heights)]
        return [el[0] for el in sorted(data, key=lambda el: el[1], reverse=True)]


if __name__ == '__main__':
    solution = Solution().sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170])
    print(solution)
