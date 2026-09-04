#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:09
FileName: 面试题/面试题 16.21. 交换和.py
Description: 
"""
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        avg = (sum1 + sum2) / 2
        if not avg.is_integer():
            return []
        avg = int(avg)
        diff1, diff2 = sum1 - avg, sum2 - avg
        for num1 in set(array1):
            for num2 in set(array2):
                if num2 - num1 == -diff1:
                    return [num1, num2]
        return []


if __name__ == '__main__':
    solution = Solution().findSwapValues(array1=[4, 1, 2, 1, 1, 2], array2=[3, 6, 3, 3])
    print(solution)
