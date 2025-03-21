#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-20 23:33
FileName: algorithm/P1441. 用栈操作构建数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if n < max(target):
            raise ValueError('Error')
        arr = []
        for i in range(1, max(target) + 1):
            arr.append('Push')
            if i not in target:
                arr.append('Pop')
        return arr


if __name__ == '__main__':
    solution = Solution().buildArray([1, 3], 3)
    ic(solution)
