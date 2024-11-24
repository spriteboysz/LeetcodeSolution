#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 09:49
FileName: P1385. 两个数组间的距离值
Description:
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum([all([abs(num1 - num2) > d for num2 in arr2]) for num1 in arr1])


if __name__ == '__main__':
    solution = Solution().findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2)
    print(solution)
