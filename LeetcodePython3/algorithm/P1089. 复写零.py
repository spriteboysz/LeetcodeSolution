#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 09:57
FileName: P1089. 复写零.py
Description:
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr1 = arr.copy()
        k = 0
        for i, ch in enumerate(arr1):
            try:
                if ch == 0:
                    arr[k] = 0
                    arr[k + 1] = 0
                    k += 2
                else:
                    arr[k] = ch
                    k += 1
            except IndexError:
                break

        print(arr)


if __name__ == '__main__':
    Solution().duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0])
