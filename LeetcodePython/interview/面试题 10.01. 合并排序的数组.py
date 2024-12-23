#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 22:46
FileName: 面试题 10.01. 合并排序的数组
Description:
"""
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        for i in range(m, m + n):
            A[i] = B[i - m]
        A.sort()
        print(A)


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
