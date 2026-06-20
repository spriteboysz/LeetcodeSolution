#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:12
FileName: P1299. 将每个元素替换为右侧最大元素.py
Description:
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maximum = maximum, max(maximum, arr[i])
        return arr


if __name__ == '__main__':
    solution = Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1])
    print(solution)
