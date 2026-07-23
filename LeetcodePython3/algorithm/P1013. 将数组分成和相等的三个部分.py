#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-22 23:10
FileName: P1013. 将数组分成和相等的三个部分.py
Description:
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        acc, index1, index2 = 0, -1, -1
        for i, num in enumerate(arr):
            acc += num
            if index1 == -1 and acc == s // 3:
                index1 = i
            elif index2 == -1 and acc == s * 2 // 3:
                index2 = i
            if index1 < index2 < len(arr) - 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().canThreePartsEqualSum([1, -1, 1, -1])
    print(solution)
