#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 08:47
FileName: P2418. 按身高排序
Description:
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = [(name, height) for name, height in zip(names, heights)]
        return list(map(lambda el: el[0], sorted(data, key=lambda el: -el[1])))


if __name__ == '__main__':
    solution = Solution().sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150])
    print(solution)
