#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:08
FileName: P1122. 数组的相对排序.py
Description:
"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda num: (dic.get(num, 1000), num))


if __name__ == '__main__':
    solution = Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6])
    print(solution)
