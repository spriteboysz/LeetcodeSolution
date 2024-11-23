#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:16
FileName: P1502. 判断能否形成等差数列
Description:
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len(set([arr[i] - arr[i - 1] for i in range(1, len(arr))])) == 1


if __name__ == '__main__':
    solution = Solution().canMakeArithmeticProgression([1, 3, 5, 7, 9])
    print(solution)
