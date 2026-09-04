#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:19
FileName: 面试题/面试题 10.01. 合并排序的数组.py
Description: 
"""
from typing import List


class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        a[m:m + n] = b
        a.sort()


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
