#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 16:46
FileName: 面试题/面试题 16.16. 部分排序.py
Description: 
"""
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        sorted_array = sorted(array)
        if sorted_array == array:
            return [-1, -1]
        i = 0
        while sorted_array[i] == array[i]:
            i += 1
        j = len(array) - 1
        while sorted_array[j] == array[j]:
            j -= 1
        return [i, j]


if __name__ == '__main__':
    solution = Solution().subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print('<None>' if not solution else f'{solution=}')
