#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 23:15
FileName: P0941. 有效的山脉数组
Description:
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        mountain = []
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                mountain.append('a')
            elif arr[i-1]>arr[i]:
                mountain.append('b')
            else:
                return False
        ss = ''.join(mountain)
        return 'ab' in ss and 'ba' not in ss


if __name__ == '__main__':
    solution = Solution().validMountainArray([0, 3, 2, 1])
    print(solution)
