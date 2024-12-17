#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 22:56
FileName: P1013. 将数组分成和相等的三个部分
Description:
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total, n = sum(arr), len(arr)
        if total % 3 != 0:
            return False
        acc, target, left, right = 0, total // 3, 0, n - 1
        for i, num in enumerate(arr):
            acc += num
            if acc == target:
                left = i
                break
        else:
            return False
        for i, num in enumerate(arr[::-1]):
            acc += num
            if acc == target * 2:
                right = n - 1 - i
                break
        else:
            return False
        return left < right - 1


if __name__ == '__main__':
    solution = Solution().canThreePartsEqualSum(arr=[1, -1, 1, -1])
    print(solution)
